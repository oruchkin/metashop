from django.http import Http404
from rest_framework.request import Request
from django.db.models.base import ModelBase

def get_object(object:ModelBase, pk:int) -> ModelBase:
    """
    Функция возвращает конкретный обьект класса который в нее 
    передают, либо поднимает ошибку, если обьекта не существует.
    """
    try:
        return object.objects.get(pk=pk)
    except object.DoesNotExist:
        raise Http404
    
def data_validator(request:Request, target_data:dict) -> dict:
    """
    Функция в которую передаются ТРЕБУЕМЫЕ для API переменные
    с их типома (type), задача функции проверить что переданны все 
    переменные и в верном формате. В конце вернет словарь:
    если в нем is_valid = False, то print(error_fields) в нем
    будут все ошибки. Если is_valid = True, то валидация пройдена.
    В parsed_data сохранены все данные в необходимом формате.
    """
    msg_list = []
    is_valid = True
    parsed_data = {}
    for i in target_data:
        error_dict = {i:target_data[i]}
        try:
            target_field = request.POST.get(i)
            if target_field:
                try:
                    target_field=(target_data[i](target_field))
                    isinstance(target_field, target_data[i])
                    parsed_data[i] = request.POST.get(i)
                except:
                    is_valid = False
                    msg_list.append(f"поле '{i}' должно быть {target_data[i]}")
            else:
                is_valid = False
                msg_list.append(f"не заполнено поле: {i}")
        except:
            is_valid = False
            msg_list.append(error_dict)
    result = {"is_valid":is_valid,
              "error_fields":msg_list,
              "parsed_data":parsed_data}
    return result