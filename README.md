# tcp-on-asm
sample code for a tcp service exposed via an Anthos Service Mesh's ingress gateway, and a locally run "client" app

this walkthrough exposes a TCP-based service on a non-standard port via ASM's ingress gateway.

## create a cluster and install ASM

```gcloud beta container --project "alexmattson-scratch" clusters create "asm-test-cluster-01" --zone "us-central1-c" --no-enable-basic-auth --cluster-version "1.17.14-gke.1600" --release-channel "regular" --machine-type "e2-standard-4" --image-type "COS" --disk-type "pd-ssd" --disk-size "100" --metadata disable-legacy-endpoints=true --scopes "https://www.googleapis.com/auth/devstorage.read_only","https://www.googleapis.com/auth/logging.write","https://www.googleapis.com/auth/monitoring","https://www.googleapis.com/auth/servicecontrol","https://www.googleapis.com/auth/service.management.readonly","https://www.googleapis.com/auth/trace.append" --max-pods-per-node "32" --num-nodes "3" --enable-stackdriver-kubernetes --enable-ip-alias --network "projects/alexmattson-scratch/global/networks/default" --subnetwork "projects/alexmattson-scratch/regions/us-central1/subnetworks/default" --default-max-pods-per-node "32" --enable-autoscaling --min-nodes "3" --max-nodes "5" --no-enable-master-authorized-networks --addons HorizontalPodAutoscaling,HttpLoadBalancing --enable-autoupgrade --enable-autorepair --max-surge-upgrade 1 --max-unavailable-upgrade 0 --workload-pool "alexmattson-scratch.svc.id.goog" --node-locations "us-central1-c"
```

```
gcloud beta container hub memberships register asm-test-cluster-01 \
   --gke-uri=https://container.googleapis.com/v1/projects/alexmattson-scratch/zones/us-central1-c/clusters/asm-test-cluster-01 \
   --enable-workload-identity
```

```
./install_asm \
  --project_id alexmattson-scratch \
  --cluster_name asm-test-cluster-01 \
  --cluster_location us-central1-c \
  --mode install \
  --output_dir ./asm-temp \
  --enable_all \
  --custom_overlay asm-setup/ig-port-overlay.yaml
```

## udpate the ingress gateway ports

this is done *after* a bunch of ASM setup previously for a cluster, and my test is on an existing ASM installation 

replace the proper values below based on your config

```
$ ./install_asm \
  --project_id alexmattson-scratch \
  --cluster_name asm-external-whereami-01 \
  --cluster_location us-central1-c \
  --mode install \
  --output_dir ./asm-external-whereami-01 \
  --enable_all \
  --custom_overlay ../tcp-on-asm/asm-setup/ig-port-overlay.yaml
```

^^^ none of this port overlay stuff works - had to edit in GKE console

