import uuid
from sqlalchemy import String, Text, ForeignKey, UniqueConstraint, JSON, Integer, Float
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.infrastructure.persistence.sqlalchemy.base import Base, pk_uuid

class FlowModel(Base):
    __tablename__ = "flows"
    id: Mapped[uuid.UUID] = pk_uuid()
    alias: Mapped[str] = mapped_column(String(120), unique=True, index=True)
    name: Mapped[str] = mapped_column(String(200))
    short_description: Mapped[str] = mapped_column(String(200))
    long_description: Mapped[str | None] = mapped_column(Text, nullable=True)
    steps: Mapped[list["FlowStepModel"]] = relationship(
        back_populates="flow",
        cascade="all, delete-orphan",
        order_by="FlowStepModel.order"
    )

class ProfileModel(Base):
    __tablename__ = "profiles"
    id: Mapped[uuid.UUID] = pk_uuid()
    name: Mapped[str] = mapped_column(String(120), unique=True, index=True)
    kind: Mapped[str] = mapped_column(String(20))
    python_version: Mapped[str | None] = mapped_column(String(20), nullable=True)
    env_vars: Mapped[dict] = mapped_column(JSON, default=dict)
    path_entries: Mapped[list[str]] = mapped_column(JSON, default=list)

class FlowStepModel(Base):
    __tablename__ = "flow_steps"
    id: Mapped[uuid.UUID] = pk_uuid()
    flow_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("flows.id", ondelete="CASCADE"), index=True)
    order: Mapped[int] = mapped_column(Integer)
    action_type: Mapped[str] = mapped_column(String(20))
    artifact_ref: Mapped[str | None] = mapped_column(String(500), nullable=True)
    args: Mapped[dict | None] = mapped_column(JSON, nullable=True)
    env: Mapped[dict | None] = mapped_column(JSON, nullable=True)
    working_dir: Mapped[str | None] = mapped_column(String(500), nullable=True)
    profile_id: Mapped[uuid.UUID | None] = mapped_column(ForeignKey("profiles.id"), nullable=True)
    ref_alias: Mapped[str | None] = mapped_column(String(120), nullable=True)
    flow: Mapped["FlowModel"] = relationship(back_populates="steps")
    __table_args__ = (UniqueConstraint("flow_id", "order", name="uq_flow_order"),)

class RunHistoryModel(Base):
    __tablename__ = "run_history"
    id: Mapped[uuid.UUID] = pk_uuid()
    flow_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("flows.id"), index=True)
    status: Mapped[str] = mapped_column(String(20))
    started_at: Mapped[float | None] = mapped_column(Float, nullable=True)
    finished_at: Mapped[float | None] = mapped_column(Float, nullable=True)
    duration_ms: Mapped[int | None] = mapped_column(Integer, nullable=True)

class RunStepRecordModel(Base):
    __tablename__ = "run_step_records"
    id: Mapped[uuid.UUID] = pk_uuid()
    run_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("run_history.id"), index=True)
    order: Mapped[int] = mapped_column(Integer)
    status: Mapped[str] = mapped_column(String(20))
    exit_code: Mapped[int | None] = mapped_column(Integer, nullable=True)
    stdout_path: Mapped[str | None] = mapped_column(String(500), nullable=True)
    stderr_path: Mapped[str | None] = mapped_column(String(500), nullable=True)
    started_at: Mapped[float | None] = mapped_column(Float, nullable=True)
    finished_at: Mapped[float | None] = mapped_column(Float, nullable=True)
    duration_ms: Mapped[int | None] = mapped_column(Integer, nullable=True)
