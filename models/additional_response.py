from pydantic import BaseModel


class AdditionalResponse(BaseModel):
    """
    Модель для хранения дополнительной информации о сущности
    для ответа.

    Attributes:
        additional_info (str): Дополнительные сведения о сущности.
        additional_number (int): Дополнительное число для сущности.
        id (int): Идентификатор дополнительной информации.
    """
    additional_info: str
    additional_number: int
    id: int
