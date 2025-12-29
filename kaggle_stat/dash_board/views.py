from django.shortcuts import render
from kaggle_stat import kaggle_service


# Вместо словаря используйте список словарей
FAKE_DATA = {
    'cards': [
        {
            'title': 'AI Mathematical Olympiad - Progress Prize 3',
            'text': '''Solve international-level math
            challenges using artificial intelligence models''',
            'image': 'path/to/image1.jpg'
        },
        {
            'title': 'Vesuvius Challenge - Surface Detection',
            'text': 'Build a model to virtually unwrap ancient scrolls.',
            'image': 'path/to/image2.jpg'
        },
        {
            'title': 'Google Tunix Hack - Train a model to show its work',
            'text': '''Teach a LLM to reason using Tunix, Google’s new JAX-native library for LLM post-training.''',
            'image': 'path/to/image1.jpg'
        },
        {
            'title': 'CSIRO - Image2Biomass Prediction',
            'text': 'Predict biomass using the provided pasture images',
            'image': 'path/to/image2.jpg'
        },
        {
            'title': 'Recod.ai/LUC - Scientific Image Forgery Detection',
            'text': '''Develop methods that can accurately detect and segment copy-move forgeries within biomedical research images.''',
            'image': 'path/to/image1.jpg'
        },
        {
            'title': 'Santa 2025 - Christmas Tree Packing Challenge',
            'text': 'How many Christmas trees can fit in a box? Help solve a classic optimization problem with a festive twist.',
            'image': 'path/to/image2.jpg'
        },
        {
            'title': 'CAFA 6 Protein Function Prediction',
            'text': '''Predict the biological function of a protein''',
            'image': 'pa    th/to/image1.jpg'
        },
        {
            'title': 'PhysioNet - Digitization of ECG Images',
            'text': 'Extract the ECG time-series data from scans and photographs of paper printouts of the ECGs.',
            'image': 'path/to/image2.jpg'
        },
        {
            'title': 'Deep Past Challenge - Translate Akkadian to English',
            'text': '''Bringing Bronze Age Voices Back to Life – Machine Translation of Old Assyrian Cuneiform''',
            'image': 'path/to/image1.jpg'
        },
        {
            'title': 'Diabetes Prediction Challenge',
            'text': 'Playground Series - Season 5, Episode 12',
            'image': 'path/to/image2.jpg'
        },
        {
            'title': 'Hull Tactical - Market Prediction',
            'text': '''Can you predict market predictability?''',
            'image': 'path/to/image1.jpg'
        },
        {
            'title': 'MITSUI&CO. Commodity Prediction Challenge',
            'text': 'Develop a robust model for accurate and stable prediction of commodity prices',
            'image': 'path/to/image2.jpg'
        },
    ]
}


def index(request):
    template = 'homepage/index.html'
    context = FAKE_DATA
    return render(request, template, context)
