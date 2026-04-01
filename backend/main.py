@app.post("/chat")
def chat(request: ChatRequest):
    user_message = request.message.lower()

    if "hello" in user_message:
        response = "Hey! I'm your Cloud Support Assistant. What can I help you with today?"
    elif "aws" in user_message:
        response = "AWS is a cloud platform offering services like EC2 (servers), S3 (storage), and more. What are you trying to do?"
    elif "ec2" in user_message:
        response = "EC2 allows you to run virtual servers in the cloud. Are you trying to launch or troubleshoot an instance?"
    elif "linux" in user_message:
        response = "Linux is commonly used in cloud environments. Are you working with commands or troubleshooting something?"
    else:
        response = "I can help with AWS, Linux, and cloud support. Try asking about EC2, S3, or troubleshooting."

    return {"response": response}
    
