from typing import List

from fastapi import APIRouter, Body, Depends, HTTPException, Path
from starlette.status import HTTP_201_CREATED, HTTP_404_NOT_FOUND  

from app.models.cleaning import CleaningCreate, CleaningUpdate, CleaningPublic 
from app.db.repositories.cleanings import CleaningsRepository  
from app.api.dependencies.database import get_repository  

router = APIRouter()

@router.get("/", response_model=List[CleaningPublic], name="cleanings:get-all-cleanings")
async def get_all_cleanings(
    cleanings_repo: CleaningsRepository = Depends(get_repository(CleaningsRepository)) 
) -> List[CleaningPublic]:
    return await cleanings_repo.get_all_cleanings() 


@router.post("/", response_model=CleaningPublic, name="cleanings:create-cleaning", status_code=HTTP_201_CREATED)
async def create_new_cleaning(
    new_cleaning: CleaningCreate = Body(..., embed=True),
    cleanings_repo: CleaningsRepository = Depends(get_repository(CleaningsRepository)),  
) -> CleaningPublic:
    created_cleaning = await cleanings_repo.create_cleaning(new_cleaning=new_cleaning)

    return created_cleaning


@router.get("/{data}/", response_model=CleaningPublic, name="cleanings:get-cleaning-by-data")
async def get_cleaning_by_data(
  data: str, cleanings_repo: CleaningsRepository = Depends(get_repository(CleaningsRepository))
) -> CleaningPublic:
    cleaning = await cleanings_repo.get_cleaning_by_data(data=data)
    if not cleaning:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="Não foi achada a data.")
    return cleaning


@router.put("/{data}/", 
    response_model=CleaningPublic, 
    name="cleanings:update-cleaning-by-data",
)
async def update_cleaning_by_data(
    data: str = Path(..., title="A data que sofrerá update."),
    cleaning_update: CleaningUpdate = Body(..., embed=True),
    cleanings_repo: CleaningsRepository = Depends(get_repository(CleaningsRepository)),
) -> CleaningPublic:
    updated_cleaning = await cleanings_repo.update_cleaning(
        data=data, cleaning_update=cleaning_update,
    )

    if not updated_cleaning:
        raise HTTPException(
            status_code=HTTP_404_NOT_FOUND, 
            detail="Não foi achada essa data.",
        )

    return updated_cleaning

@router.delete("/{data}/", response_model=int, name="cleanings:delete-cleaning-by-data")
async def delete_cleaning_by_data(
    data: str = Path(..., title="A data que será excluida."),
    cleanings_repo: CleaningsRepository = Depends(get_repository(CleaningsRepository)),
) -> int:
    deleted_id = await cleanings_repo.delete_cleaning_by_data(data=data)
    if not deleted_data:
        raise HTTPException(
            status_code=HTTP_404_NOT_FOUND, 
            detail="Não foi achada essa data.",
        )
    return deleted_id