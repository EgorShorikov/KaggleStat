from django.shortcuts import render
from kaggle_service import KaggleService


FAKE_DATA = {
    'cards': [
        {
            'title': 'AI Mathematical Olympiad - Progress Prize 3',
            'description': '''Solve international-level math
            challenges using artificial intelligence models''',
            'image': "https://storage.googleapis.com/kaggle-competitions/kaggle/118448/logos/thumb76_76.png?GoogleAccessId=web-data@kaggle-161607.iam.gserviceaccount.com&Expires=1767396698&Signature=lBD3AmTG8MfpJcpYPLQygHfvlaQCKGvLZ355TGdcpzV8ksgrlFQLQvEIufd098aG%2BK8oiuNpHBlVzJgaLKgekO0WK5pX0T8pVTPaS98VzjYfbM9PNAEXTBlRcw9hnaP8ZuB%2FoAKpTb3qGvs3LaLk5hOsSsgv4d0P5nq3rsiyLb%2FykglL09j9Ap5kWPDsP4J9KAPCMZd8rIFW9l7NqAZiQR9%2FAdZT4xabIUCq%2BWJyYnuqQnxzyjY%2Fezu9oHI52K3l9m0jF0fVgZ6BizBFRyOEGcs0JX8Yc3DBdEJK6u7KNqjuCsToG3APlDIPpyRETntljoYrgA4hsr5f0sMTHcp0sA%3D%3D",
            'prize': 10000
        },
        {
            'title': 'Vesuvius Challenge - Surface Detection',
            'description': 'Build a model to virtually unwrap ancient scrolls.',
            'image': 'https://storage.googleapis.com/kaggle-competitions/kaggle/118448/logos/thumb76_76.png?GoogleAccessId=web-data@kaggle-161607.iam.gserviceaccount.com&Expires=1767142893&Signature=YYMv9jbTkz%2BKpLrhAJqbUZkqlFlyhyKXFRgnOQ02uMKogDyUZb3reQxD%2BlM0rcXn98UNfwMF9qF3VYYqa5uUs6mY7zHdaEJxKa2Zd9Q7kraEv3jlNrmcEI0r4zeghkLqa%2F63eMHhEhlmBnme9RiUzkvhsOhvoEPo2oUBkEvzzgTuXk5dQsFpb7EOa%2FZdsnpNvorAzg%2FJRvS9fENnjmLaxHyIyr8HucghNCbJQQzhIVkjHZfd2LMgr5C0I8ZNBnYZJayDIEuKd3jLoMsnScpWorlVFXxqbdz6Y4WmzBFpkuUSNj48ZK15yaI%2BtNQwbH8Vqa%2Bn735l2%2BuXsG530F08Rg%3D%3D',
            'prize': 10000
        },
        {
            'title': 'Google Tunix Hack - Train a model to show its work',
            'description': '''Teach a LLM to reason using Tunix, Google’s new JAX-native library for LLM post-training.''',
            'image': 'https://storage.googleapis.com/kaggle-competitions/kaggle/3136/logos/thumb76_76.png?GoogleAccessId=web-data@kaggle-161607.iam.gserviceaccount.com&Expires=1767142862&Signature=lXzVVqTm63jRAZwIn%2Byik1vnDTguv1CYBCYWenuWncS7IqLwyWWa2PNTzGFMQdEQSC5aOZFAsJ0NaHvSmDl07lr%2FqAfmyfgh5T5RSXwA07pFPh6lBnS4sBlQuvRpHz6zsd1604kqLPTrB3D5N6PwpSSs%2BqJXP0TB6KJGw38ibHH0thv7EB01RXYwZdzrFeTLNG7%2BAf2T1SMqjqH2qekkEgQBWVETwB3GvzX7fUdOyFfVrRGzsNtC%2BjZGuDEwxWQf4%2BWsEcXYcaT8raqctnXmyCN1RQeI3vnA5lf5rDkVtgxsuCIfrtElTPqU7bZgTtDgNP2TLco%2BNPC9TXIHQ7RD4g%3D%3D',
            'prize': 10000
        },
        {
            'title': 'CSIRO - Image2Biomass Prediction',
            'description': 'Predict biomass using the provided pasture images',
            'image': 'path/to/image2.jpg'
        },
        {
            'title': 'Recod.ai/LUC - Scientific Image Forgery Detection',
            'description': '''Develop methods that can accurately detect and segment copy-move forgeries within biomedical research images.''',
            'image': 'path/to/image1.jpg'
        },
        {
            'title': 'Santa 2025 - Christmas Tree Packing Challenge',
            'description': 'How many Christmas trees can fit in a box? Help solve a classic optimization problem with a festive twist.',
            'image': 'path/to/image2.jpg'
        },
        {
            'title': 'CAFA 6 Protein Function Prediction',
            'description': '''Predict the biological function of a protein''',
            'image': 'pa    th/to/image1.jpg'
        },
        {
            'title': 'PhysioNet - Digitization of ECG Images',
            'description': 'Extract the ECG time-series data from scans and photographs of paper printouts of the ECGs.',
            'image': 'path/to/image2.jpg'
        },
        {
            'title': 'Deep Past Challenge - Translate Akkadian to English',
            'description': '''Bringing Bronze Age Voices Back to Life – Machine Translation of Old Assyrian Cuneiform''',
            'image': 'path/to/image1.jpg'
        },
        {
            'title': 'Diabetes Prediction Challenge',
            'description': 'Playground Series - Season 5, Episode 12',
            'image': 'path/to/image2.jpg'
        },
        {
            'title': 'Hull Tactical - Market Prediction',
            'description': '''Can you predict market predictability?''',
            'image': 'path/to/image1.jpg'
        },
        {
            'title': 'MITSUI&CO. Commodity Prediction Challenge',
            'description': 'Develop a robust model for accurate and stable prediction of commodity prices',
            'image': 'path/to/image2.jpg'
        },
    ]
}


def index(request):
    r"""
  Attributes:
    id (int)
    ref (str)
    title (str)
    url (str)
    description (str)
    organization_name (str)
    organization_ref (str)
    category (str)
    reward (str)
    tags (ApiCategory)
    deadline (datetime)
    kernel_count (int)
    team_count (int)
    user_has_entered (bool)
    user_rank (int)
    merger_deadline (datetime)
    new_entrant_deadline (datetime)
    enabled_date (datetime)
    max_daily_submissions (int)
    max_team_size (int)
    evaluation_metric (str)
    awards_points (bool)
    is_kernels_submissions_only (bool)
    submissions_disabled (bool)
    thumbnail_image_url (str)
    host_name (str)
  """
    kaggle_service = KaggleService()
    real_data = []
    competitions = kaggle_service.get_all_competitions(sort_by='prize')[:12]
    for competition in competitions:
        competition_info = {
            'kaggle_slug': competition.ref.split('/')[-1],
            'title': competition.title,
            'deadline': competition.deadline,
            'participant_count': competition.team_count,
            'prize': competition.reward,
            'description': competition.description
        }
        real_data.append(competition_info)
    template = 'homepage/index.html'
    context = {"competitions": real_data}
    return render(request, template, context)
