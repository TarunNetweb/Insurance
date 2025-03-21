from fastapi import APIRouter
from controllers.policy_controller import router as policy_router

router = APIRouter()
router.include_router(policy_router, prefix="/policy", tags=["Policy Management"])