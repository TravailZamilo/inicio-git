INSTANCE_ID=$(aws ec2 describe-instances --query "Reservations[*].Instances[?Tags[?Key=='Name'&&contains(Value,'Jupyter')]].InstanceId" --output text)

IP=$(aws ec2 describe-instances --instance-ids $INSTANCE_ID --query 'Reservations[*].Instances[*].PublicIpAddress' --output text)

TOKEN=$(jq -r '.token' /home/ec2-user/.local/share/jupyter/runtime/jpserver*.json)

echo http://$IP:8888/lab?token=$TOKEN