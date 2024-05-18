import runpod  # Required.


def handler(job):
    job_input = job["input"]  # Access the input from the request.
    # Add your custom code here.
    return f"Echo: {job_input}"


runpod.serverless.start({
    "handler": handler
})
