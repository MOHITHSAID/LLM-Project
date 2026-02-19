import torch
import torch.nn as nn
from torchvision import models, transforms
from PIL import Image

NUM_CLASSES = 24

CLASS_NAMES = [
    "Ajanta Caves",
    "alai_darwaza",
    "alai_minar",
    "basilica_of_bom_jesus",
    "Charar-E-Sharif",
    "charminar",
    "Chhota_Imambara",
    "Ellora Caves",
    "Fatehpur Sikri",
    "Gateway of India",
    "golden temple",
    "hawa mahal pics",
    "Humayun_s Tomb",
    "India gate pics",
    "iron_pillar",
    "jamali_kamali_tomb",
    "Khajuraho",
    "lotus_temple",
    "mysore_palace",
    "qutub_minar",
    "Sun Temple Konark",
    "tajmahal",
    "tanjavur temple",
    "victoria memorial"
]

model = models.resnet18(weights=None)
model.fc = nn.Linear(model.fc.in_features, NUM_CLASSES)

model.load_state_dict(
    torch.load(r"vision\resnet_monument_model.pth", map_location="cpu")
)

model.eval()

transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
])

def predict_image(image_path):
    image = Image.open(image_path).convert("RGB")
    image = transform(image).unsqueeze(0)

    with torch.no_grad():
        outputs = model(image)
        probabilities = torch.softmax(outputs, dim=1)
        confidence, predicted = torch.max(probabilities, 1)

    predicted_class = CLASS_NAMES[predicted.item()]
    confidence_score = confidence.item()

    return predicted_class, confidence_score
