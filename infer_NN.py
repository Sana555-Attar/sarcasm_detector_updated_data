from clearml import Model, Task
import joblib
import sys 

sys.modules['sklearn.externals.joblib'] = joblib

tsk = Task.init('sarcasm_detector','SKLEARN model inference ','inference')

sklearn_model_path = Model(model_id="8c76f34b0c6d47818c1ee70d1708dc2e").get_local_copy()

sklearn_pipeline = joblib.load(sklearn_model_path)

args = {'sentences' : ["Coworkers At Bathroom Sink Locked In Tense Standoff Over Who Going To Wash Hands Longer","grandma jumps into buick for emergency birdseed run"]}
tsk.connect(args)

scores = sklearn_pipeline.predict_proba(args['sentences'])

print(f"Input Sentences :\n{args['sentences']}")

for idx, score in enumerate(scores):
    score = score[0]
    if score < 0.5:
        label = 'NORMAL'
        score = 1 - score
    else:
        label = 'SARCASTIC'
    print(f"Commnet: {args['sentences'][idx]}\nLABEL: {label}\nCERTAINTY: {score:.2f}\n")

tsk.close()
    
