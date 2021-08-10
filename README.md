
## Table of Contents

1. Application Overview
2. [ Installation Steps ](#runtheapplication)


<a name="assetdescription"></a>
## 1. Face mask detection API



<a name="runtheapplication"></a>
## 4. Installation Steps
 * Make sure that, Openshift Pipeline is installed on your cluster. 
 * Pipeline client is installed on your local system(tkn cli)
 * Login into your target openshift cluster.
 * Clone this repository on your local folder.
 * Change to directory deployscripts. Ex: cd deployscripts
 * Execute the startbuid.sh ex: ./startbuild.sh this will install the pipeline and start the pipeline.
 * Once the above step is completed, the application will be deployed on your cluster.
 * Expose the service through route. Ex: oc expose svc mask-detection
