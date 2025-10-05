from typing import List
from app.domain.entities.run_history import RunHistory
from app.domain.entities.run_step_record import RunStepRecord
from app.domain.repositories.run_history_repository import RunHistoryRepository
from app.infrastructure.persistence.sqlalchemy.connection import SessionLocal
from app.infrastructure.persistence.sqlalchemy.models import RunHistoryModel, RunStepRecordModel

class SqlAlchemyRunHistoryRepository(RunHistoryRepository):
    def create_run(self, run: RunHistory) -> RunHistory:
        with SessionLocal() as session:
            db = RunHistoryModel(flow_id=run.flow_id, status=run.status, started_at=run.started_at, finished_at=run.finished_at, duration_ms=run.duration_ms)
            session.add(db)
            session.commit()
            session.refresh(db)
            return RunHistory(id=db.id, flow_id=db.flow_id, status=db.status, started_at=db.started_at, finished_at=db.finished_at, duration_ms=db.duration_ms)

    def update_run(self, run: RunHistory) -> None:
        with SessionLocal() as session:
            session.query(RunHistoryModel).filter(RunHistoryModel.id == run.id).update(dict(status=run.status, started_at=run.started_at, finished_at=run.finished_at, duration_ms=run.duration_ms))
            session.commit()

    def append_step_record(self, record: RunStepRecord) -> RunStepRecord:
        with SessionLocal() as session:
            db = RunStepRecordModel(run_id=record.run_id, order=record.order, status=record.status, exit_code=record.exit_code, stdout_path=record.stdout_path, stderr_path=record.stderr_path, started_at=record.started_at, finished_at=record.finished_at, duration_ms=record.duration_ms)
            session.add(db)
            session.commit()
            session.refresh(db)
            return RunStepRecord(id=db.id, run_id=db.run_id, order=db.order, status=db.status, exit_code=db.exit_code, stdout_path=db.stdout_path, stderr_path=db.stderr_path, started_at=db.started_at, finished_at=db.finished_at, duration_ms=db.duration_ms)

    def list_by_flow(self, flow_id: int) -> List[RunHistory]:
        with SessionLocal() as session:
            rows = session.query(RunHistoryModel).filter(RunHistoryModel.flow_id == flow_id).all()
            return [RunHistory(id=r.id, flow_id=r.flow_id, status=r.status, started_at=r.started_at, finished_at=r.finished_at, duration_ms=r.duration_ms) for r in rows]
