

import dlib
import numpy as np
import face_recognition_models
import streamlit as st

from src.database.db import get_all_students


FACE_MATCH_THRESHOLD = 0.45
FACE_MATCH_MARGIN = 0.05


@st.cache_resource
def load_dlib_models():
    detector = dlib.get_frontal_face_detector() 


    sp = dlib.shape_predictor(
        face_recognition_models.pose_predictor_model_location()
    )

    facerec = dlib.face_recognition_model_v1(
        face_recognition_models.face_recognition_model_location()
    )

    return detector, sp, facerec

def get_face_embeddings(image_np):
    detector, sp, facerec = load_dlib_models()
    faces = detector(image_np, 1)

    encodings= []

    for face in faces:
        shape = sp(image_np, face)
        face_descriptor = facerec.compute_face_descriptor(image_np, shape, 1) #128 embedding

        encodings.append(np.array(face_descriptor))
    return encodings

@st.cache_resource
def get_trained_model():
    embeddings = []
    student_ids = []
    student_db = get_all_students()

    if not student_db:
        return None
    
    for student in student_db:
        embedding = student.get('face_embedding')
        if embedding:
            embedding = np.asarray(embedding, dtype=np.float64)
            if embedding.shape == (128,) and np.all(np.isfinite(embedding)):
                embeddings.append(embedding)
                student_ids.append(int(student['student_id']))

    if not embeddings:
        return None

    return {
        'embeddings': np.vstack(embeddings),
        'student_ids': np.asarray(student_ids, dtype=np.int64),
    }


def train_classifier():
    st.cache_resource.clear()
    model_data = get_trained_model()
    return bool(model_data)

def predict_attendance(class_image_np):
    encodings = get_face_embeddings(class_image_np)

    detected_student = {}


    model_data = get_trained_model()

    if not model_data:
        return detected_student, [], len(encodings)
    
    known_ids = model_data['student_ids']
    known_embeddings = model_data['embeddings']
    all_students = sorted(set(known_ids.tolist()))

    for encoding in encodings:
        distances = np.linalg.norm(known_embeddings - encoding, axis=1)
        closest_by_student = {
            student_id: float(np.min(distances[known_ids == student_id]))
            for student_id in all_students
        }
        ranked_matches = sorted(closest_by_student.items(), key=lambda item: item[1])

        best_id, best_distance = ranked_matches[0]
        has_clear_margin = (
            len(ranked_matches) == 1
            or ranked_matches[1][1] - best_distance >= FACE_MATCH_MARGIN
        )

        if best_distance <= FACE_MATCH_THRESHOLD and has_clear_margin:
            detected_student[best_id] = True
    return detected_student, all_students, len(encodings)
