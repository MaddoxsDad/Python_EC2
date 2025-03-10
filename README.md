# AWS EC2 Connection Script

## 📖 Overview
This Python script connects to AWS EC2 using the **boto3** library, allowing users to:  
✅ List running EC2 instances  
✅ Start an EC2 instance  
✅ Stop an EC2 instance  

---

## 🚀 Prerequisites

### 1️⃣ Install Python (if not installed)
Ensure you have Python 3 installed. Check with:
```sh
python --version
```
If not installed, download it from [Python's official site](https://www.python.org/).

### 2️⃣ Install boto3 (AWS SDK for Python)
Install boto3 using pip:
```sh
pip install boto3
```

### 3️⃣ Configure AWS Credentials
You need AWS access keys to authenticate. Configure them using:
```sh
aws configure
```
Provide:  
- **AWS Access Key ID**  
- **AWS Secret Access Key**  
- **Default region** (e.g., `us-east-1`)  

Alternatively, you can manually set them in `~/.aws/credentials`.

---

## 📜 How to Use

1️⃣ Clone the repository:
```sh
git clone https://github.com/your-username/aws-ec2-connector.git
cd aws-ec2-connector
```

2️⃣ Run the script:
```sh
python aws_ec2_connect.py
```

3️⃣ Optional: Modify the script to start/stop an instance by replacing `your-instance-id-here` in:
```python
# instance_id = "your-instance-id-here"
# start_instance(instance_id)
# stop_instance(instance_id)
```

---

## 🛠 Features
- ✅ List all running EC2 instances
- ✅ Start an EC2 instance
- ✅ Stop an EC2 instance
- ✅ Easy AWS authentication with `boto3`

---

## 📌 Notes
- Ensure that your IAM user has **EC2 permissions** (`ec2:DescribeInstances`, `ec2:StartInstances`, `ec2:StopInstances`).  
- Modify the `region_name` in `boto3.client("ec2", region_name="us-east-1")` if needed.

---

## 📜 License
This project is open-source and available under the [MIT License](LICENSE).

---

## 💡 Contributing
Feel free to fork this project and submit a pull request! 🚀  

---

## 📞 Contact
For any issues, open an [issue](https://github.com/your-username/aws-ec2-connector/issues) on GitHub or reach out to me at [your-email@example.com](mailto:your-email@example.com).

---

### ⭐ **If you find this useful, give it a star!** ⭐
