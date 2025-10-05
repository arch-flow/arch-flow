from typing import List, Optional
from app.domain.entities.flow import Flow
from app.domain.entities.flow_step import FlowStep
from app.domain.repositories.flow_repository import FlowRepository
from app.infrastructure.persistence.sqlalchemy.connection import SessionLocal
from app.infrastructure.persistence.sqlalchemy.models import FlowModel, FlowStepModel

class SqlAlchemyFlowRepository(FlowRepository):
    def create(self, flow: Flow) -> Flow:
        with SessionLocal() as session:
            db_flow = FlowModel(alias=flow.alias, name=flow.name, short_description=flow.short_description, long_description=flow.long_description)
            for s in flow.steps:
                db_flow.steps.append(FlowStepModel(order=s.order, action_type=s.action_type, artifact_ref=s.artifact_ref, args=s.args, env=s.env, working_dir=s.working_dir, profile_id=s.profile_id, ref_alias=s.ref_alias))
            session.add(db_flow)
            session.commit()
            session.refresh(db_flow)
            return Flow(id=db_flow.id, alias=db_flow.alias, name=db_flow.name, short_description=db_flow.short_description, long_description=db_flow.long_description, steps=[FlowStep(id=ds.id, flow_id=db_flow.id, order=ds.order, action_type=ds.action_type, artifact_ref=ds.artifact_ref, args=ds.args, env=ds.env, working_dir=ds.working_dir, profile_id=ds.profile_id, ref_alias=ds.ref_alias) for ds in db_flow.steps])

    def get_by_alias(self, alias: str) -> Optional[Flow]:
        with SessionLocal() as session:
            db_flow = session.query(FlowModel).filter(FlowModel.alias == alias).first()
            if not db_flow:
                return None
            return Flow(id=db_flow.id, alias=db_flow.alias, name=db_flow.name, short_description=db_flow.short_description, long_description=db_flow.long_description, steps=[FlowStep(id=ds.id, flow_id=db_flow.id, order=ds.order, action_type=ds.action_type, artifact_ref=ds.artifact_ref, args=ds.args, env=ds.env, working_dir=ds.working_dir, profile_id=ds.profile_id, ref_alias=ds.ref_alias) for ds in db_flow.steps])

    def list_all(self) -> List[Flow]:
        with SessionLocal() as session:
            db_flows = session.query(FlowModel).all()
            result = []
            for f in db_flows:
                steps = [FlowStep(id=s.id, flow_id=f.id, order=s.order, action_type=s.action_type, artifact_ref=s.artifact_ref, args=s.args, env=s.env, working_dir=s.working_dir, profile_id=s.profile_id, ref_alias=s.ref_alias) for s in f.steps]
                result.append(Flow(id=f.id, alias=f.alias, name=f.name, short_description=f.short_description, long_description=f.long_description, steps=steps))
            return result
