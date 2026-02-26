from django.http import JsonResponse
from django.shortcuts import render
from .models import FatigueLog
import json

def dashboard(request):
    return render(request, "dashboard.html")

def save_fatigue(request):
    if request.method == "POST":
        data = json.loads(request.body)

        FatigueLog.objects.create(
            blink_rate=data["blink_rate"],
            fatigue_score=data["fatigue_score"]
        )

        return JsonResponse({"status": "saved"})