headers = {
    "Content-Type": "application/json"
}

user_body = {
    "firstName": "Анатолий",
    "phone": "+79995553322",
    "address": "г. Москва, ул. Пушкина, д. 10"
}

kit_body = {
       "name": "Мой набор",
       "card": {
           "id": 1,
           "name": "Под ситуацию"
       },
       "productsList": [
               {
                   "id": 1,
                   "name": "Сок Jumex апельсин без сахара",
                   "price": 149,
                   "weight": 473,
                   "units": "мл",
                   "quantity": 1
               },
               {
                   "id": 2,
                   "name": "Evervess Тоник напиток сильногазированный",
                   "price": 89,
                   "weight": 1,
                   "units": "л",
                   "quantity": 1
               }
           ],
       "productsCount": 2
   }
