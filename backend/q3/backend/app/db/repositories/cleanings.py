from typing import List 
from app.db.repositories.base import BaseRepository
from app.models.cleaning import CleaningCreate, CleaningUpdate, CleaningInDB


CREATE_CLEANING_QUERY = """
    INSERT INTO cleanings (data, hora, cleaning_type)
    VALUES (:data, :hora, :cleaning_type)
    RETURNING id, data, hora, cleaning_type;
"""
GET_CLEANING_BY_DATA_QUERY = """
    SELECT id, data, hora, cleaning_type
    FROM cleanings
    WHERE data = :data;
"""

GET_ALL_CLEANINGS_QUERY = """
    SELECT id, data, hora, cleaning_type  
    FROM cleanings;  
"""

UPDATE_CLEANING_BY_DATA_QUERY = """
    UPDATE cleanings  
    SET data         = :data,  
        hora  = :hora,   
        cleaning_type = :cleaning_type  
    WHERE data = :data  
    RETURNING id, data, hora, cleaning_type;  
"""

DELETE_CLEANING_BY_DATA_QUERY = """
    DELETE FROM cleanings  
    WHERE data = :data  
    RETURNING data;  
""" 

class CleaningsRepository(BaseRepository):
    
    async def create_cleaning(self, *, new_cleaning: CleaningCreate) -> CleaningInDB:
        query_values = new_cleaning.dict()
        cleaning = await self.db.fetch_one(query=CREATE_CLEANING_QUERY, values=query_values)
        return CleaningInDB(**cleaning)
    async def get_cleaning_by_data(self, *, data: str) -> CleaningInDB:
        cleaning = await self.db.fetch_one(query=GET_CLEANING_BY_DATA_QUERY, values={"data": data})
        if not cleaning:
            return None
        return CleaningInDB(**cleaning)

    async def get_all_cleanings(self) -> List[CleaningInDB]:
        cleaning_records = await self.db.fetch_all(
            query=GET_ALL_CLEANINGS_QUERY,
        )
        return [CleaningInDB(**l) for l in cleaning_records]   

    async def update_cleaning(
        self, *, data: str, cleaning_update: CleaningUpdate,
    ) -> CleaningInDB:
        cleaning = await self.get_cleaning_by_data(data=data)
        if not cleaning:
            return None
        cleaning_update_params = cleaning.copy(
            update=cleaning_update.dict(exclude_unset=True),
        )
        if cleaning_update_params.cleaning_type is None:
            raise HTTPException(
                status_code=HTTP_400_BAD_REQUEST, 
                detail="tipo invalido de dados. Nao pode ser feito.",
            )

        try:
            updated_cleaning = await self.db.fetch_one(
                query=UPDATE_CLEANING_BY_DATA_QUERY, 
                values=cleaning_update_params.dict(),
            )
            return CleaningInDB(**updated_cleaning)
        except Exception as e:
            print(e)
            raise HTTPException(
                status_code=HTTP_400_BAD_REQUEST, 
                detail="Parametros invalidos.",
            )
            
    async def delete_cleaning_by_data(self, *, data: str) -> str:
        cleaning = await self.get_cleaning_by_data(data=data)
        if not cleaning:
            return None
        deleted_id = await self.db.execute(
            query=DELETE_CLEANING_BY_DATA_QUERY, 
            values={"data": data},
        )
        return deleted_id