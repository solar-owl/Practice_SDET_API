from pydantic import BaseModel


class AdditionalRequest(BaseModel):
    """
    Модель для хранения дополнительной информации о сущности
    для запроса.

    Attributes:
        additional_info (str): Дополнительные сведения о сущности.
        additional_number (int): Дополнительное число для сущности.
    """
    additional_info: str
    additional_number: int
