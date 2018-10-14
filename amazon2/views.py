from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.template import loader

def index(request):
    return render(request, 'index.html', {})

def description(request, id = None):
    # book = Books.object.get(id= id)
    return render(request, 'description.html', {
        "owner_name": "German Rodriguez",
        "book_title": "Pet Sematary",
        "book_rating": 4,
        "book_condition": "new",
        "book_description": """Louis Creed, a doctor from Chicago, is appointed director of the University of Maine's campus health service. He moves to a large house near the small town of Ludlow with his wife Rachel, their two young children, Ellie and Gage, and Ellie's cat, Church. From the moment they arrive, the family runs into trouble: Ellie hurts her knee after falling off a swing, and Gage is stung by a bee. Their new neighbor, an elderly man named Jud Crandall, comes to help. He warns Louis and Rachel about the highway that runs past their house; it is constantly used by speeding trucks.
                  Jud and Louis quickly become close friends. Since Louis' father died when he was three, he sees Jud as a surrogate father. A few weeks after the Creeds move in, Jud puts the friendship on the line when he takes the family on a walk in the woods behind their home. A well-tended path leads to a pet cemetery (misspelled "sematary" on the sign) where the children of the town bury their deceased animals. The outing provokes a heated argument between Louis and Rachel the next day. Rachel disapproves of discussing death, and she worries about how Ellie may be affected by what she saw at the "sematary". (It is explained later that Rachel was traumatized by the early death of her sister, Zelda, from spinal meningitis—an issue that is brought up several times in flashbacks. Louis empathizes with his wife, realizing that the fault for her trauma rests with her parents, who left Rachel at home alone with her sister when she died.)
                  """
    })