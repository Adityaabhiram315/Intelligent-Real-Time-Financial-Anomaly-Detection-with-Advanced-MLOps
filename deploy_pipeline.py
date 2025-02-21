import kfp.dsl as dsl
from kfp.components import create_component_from_func

def deploy_model():
    print("Deploying model with Kubeflow...")
    # Add deployment logic here

deploy_component = create_component_from_func(deploy_model)

@dsl.pipeline(name='Financial Anomaly Detection Pipeline')
def anomaly_detection_pipeline():
    deploy_task = deploy_component()

dsl.Compiler().compile(anomaly_detection_pipeline, 'pipeline.yaml')