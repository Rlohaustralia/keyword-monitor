from django.views.decorators.csrf import csrf_exempt
from db_connection import db
import json
from django.http import JsonResponse
from django.utils.timezone import now

reference_collection = db['reference_keyword']

@csrf_exempt
def add_reference_keywords(request):
    if request.method == 'POST':
        try:
   
            data = json.loads(request.body)
            user = data.get('user')
            ref_keywords = data.get('ref_keywords')

        
            if not user or not ref_keywords:
                return JsonResponse({'error': 'user and keywords are required'}, status=400)
            
          
            existing_doc = reference_collection.find_one({"user": user})

            if existing_doc:
                
                reference_collection.update_one(
                    {"user": user},
                    {"$set": {"ref_keywords": ref_keywords, "created_at": now()}}
                )
                return JsonResponse({"message": "Successfully updated!"}, status=200)
            else:

                document = {
                    'user': user,
                    'ref_keywords': ref_keywords,
                    'created_at': now()
                }
                reference_collection.insert_one(document)
                return JsonResponse({"message": "Successfully added!"}, status=201)

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Only POST method is allowed'}, status=405)



    