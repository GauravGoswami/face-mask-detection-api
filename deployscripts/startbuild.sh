
tkn pipeline start fscloud-asset-pipeline -w name=shared-workspace,claimName=source-pvc -p deployment-name=mask-detection -p  git-url=https://github.ibm.com/IBM-India-CTO-ENG-Assets/FundtransferService.git  -p IMAGE=image-registry.openshift-image-registry.svc:5000/ml-assets/mask-detection -p git-revision=master  -p helm-git-revision=main  -p sourcerepo=src -p targetrepo=helmrepo -p git-helm-url=https://github.com/rameshpoomalai/mcmrepo.git