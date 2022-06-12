# #################### CLEAN UP #########################
echo "Setting up security account"
echo "Switching AWS profile to demo Account"
# export AWS_PROFILE=demo
echo "Switching terraform workspace to demo workspace"
terraform workspace select demo
cd terraform
echo "Clean up automation in demo Account"
terraform destroy -var-file="demo.tfvars" -auto-approve

# ###################### SET UP #########################
echo "Setting up security account"
echo "Switching AWS profile to demo Account"
# export AWS_PROFILE=demo
echo "Switching terraform workspace to demo workspace"
terraform workspace select demo
cd terraform
echo "Clean up automation in demo Account"
terraform apply -var-file="demo.tfvars" -auto-approve
