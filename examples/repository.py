from uuid import UUID


from .dto import SessionDTO
from .models import SessionCacheModel


class SessionRepository:
    def create(self, data: SessionDTO) -> SessionCacheModel:
        return SessionCacheModel.save(
            user_id=data.user_id, 
            role=data.role,
        )

    def get(self, uid: UUID) -> SessionCacheModel | None:
        return SessionCacheModel.get(uid=uid)

    def update(self, uid: UUID, data: SessionDTO) -> SessionCacheModel | None:
        s = SessionCacheModel.get(uid)
        if s is None:
            return None

        s.user_id = data.user_id
        s.role = data.role
        s.save()
        return s

    def delete(self, uid: UUID) -> bool:
        s = SessionCacheModel.get(uid)
        if s is None:
            return False

        s.delete()
        return True
