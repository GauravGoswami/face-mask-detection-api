oc create -f pipeline.yaml
oc create -f striggerevents.yaml
tkn pipeline start fscloud-asset-pipeline -w name=shared-workspace,claimName=source-pvc -p deployment-name=mask-detection -p  git-url=https://github.com/GauravGoswami/face-mask-detection-api.git  -p IMAGE=image-registry.openshift-image-registry.svc:5000/ml-assets/mask-detection -p git-revision=master  -p helm-git-revision=main  -p sourcerepo=src -p targetrepo=helmrepo -p git-helm-url=https://github.com/rameshpoomalai/mcmrepo.git
