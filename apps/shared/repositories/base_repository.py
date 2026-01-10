from typing import Type, TypeVar, Generic, List
from uuid import UUID

from sqlalchemy import select
from sqlalchemy.orm import Session

Entity = TypeVar("Entity")
Model = TypeVar("Model")


class BaseRepository(Generic[Entity, Model]):
    def __init__(self, session: Session, model_class: Type[Model]):
        self.session = session
        self.model_class = model_class

    def create(self, entity: Entity) -> None:
        db_obj = self.model_class.from_entity(entity)
        self.session.add(db_obj)
        self.session.commit()

    def list_paginated(self, offset: int, limit: int) -> List[Entity]:
        results = (
            self.session.execute(
                select(self.model_class)
                .offset(offset)
                .limit(limit)
            ).scalars().all()
        )
        return [row.to_entity() for row in results]

    def get_by_id(self, entity_id: UUID) -> Entity | None:
        db_obj = (
            self.session.query(self.model_class)
            .filter_by(id=str(entity_id))
            .first()
        )
        if db_obj:
            return db_obj.to_entity()
        return None

    def update(self, entity: Entity) -> None:
        db_obj = (
            self.session.query(self.model_class)
            .filter_by(id=str(entity.id))
            .first()
        )
        if not db_obj:
            return
        self._apply_update(entity, db_obj)
        self.session.commit()

    def delete(self, entity: Entity) -> None:
        obj = self.session.query(self.model_class).get(str(entity.id))
        if obj:
            self.session.delete(obj)
            self.session.commit()

    def exists(self, entity_id: UUID) -> bool:
        return (
                self.session.query(self.model_class)
                .filter_by(id=str(entity_id))
                .first()
                is not None
        )

    def _apply_update(self, entity: Entity, db_obj: Model) -> None:
        raise NotImplementedError()
