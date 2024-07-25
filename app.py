try:
    from langchain_ollama import ChatOllama
except ImportError:
    from langchain_community.chat_models.ollama import ChatOllama


def setup_ollama_llm(messages):
    llm = ChatOllama(
        model="phi3:latest",
        verbose=True
    )
    print("===== invoke START =====")
    formated_invoke_response_metadata = format_response_metadata(
        llm.invoke(messages).response_metadata.items()
    )
    print_result(formated_invoke_response_metadata)
    print("===== invoke END =====\n")

    print("===== stream START =====")
    for chunk in llm.stream(messages):
        if chunk.response_metadata == {}:
            continue
        formated_stream_response_metadata = format_response_metadata(
            chunk.response_metadata.items()
        )
        print_result(formated_stream_response_metadata)

    print("===== stream END =====")


def format_response_metadata(response_metadata: dict) -> dict:
    formated_response_metadata: dict = {}
    for key, value in response_metadata:
        if (key == "model"):
            model = value
            formated_response_metadata[key] = model
        elif (key == "total_duration"):
            total_duration = float(value)/(10**6)
            formated_response_metadata[key] = total_duration
        elif (key == "load_duration"):
            load_duration = float(value)/(10**6)
            formated_response_metadata[key] = load_duration
        elif (key == "prompt_eval_count"):
            prompt_eval_count = int(value)
            formated_response_metadata[key] = prompt_eval_count
        elif (key == "prompt_eval_duration"):
            prompt_eval_duration = float(value)/(10**6)
            formated_response_metadata[key] = prompt_eval_duration
        elif (key == "eval_count"):
            eval_count = int(value)
            formated_response_metadata[key] = eval_count
        elif (key == "eval_duration"):
            eval_duration = float(value)/(10**6)
            formated_response_metadata[key] = eval_duration
    return formated_response_metadata


def print_result(formated_response_metadata: dict):
    model = formated_response_metadata["model"]
    total_duration = formated_response_metadata["total_duration"]
    load_duration = formated_response_metadata["load_duration"]
    prompt_eval_count = formated_response_metadata["prompt_eval_count"]
    prompt_eval_duration = formated_response_metadata["prompt_eval_duration"]
    prompt_eval_rate = (prompt_eval_count * 1000 / prompt_eval_duration)
    eval_count = formated_response_metadata["eval_count"]
    eval_duration = formated_response_metadata["eval_duration"]
    eval_rate = (eval_count / eval_duration) * 1000

    print(f"model:                {model}")
    print(f"total duration:       {total_duration:.2f} ms")
    print(f"load duration:        {load_duration:.2f} ms")
    print(f"prompt eval count:    {prompt_eval_count} tokens")
    print(f"prompt eval duration: {prompt_eval_duration:.2f} ms")
    print(f"prompt eval rate:     {prompt_eval_rate:.2f} (tokens/s)")
    print(f"eval count:           {eval_count} tokens")
    print(f"eval duration:        {eval_duration:.2f} ms")
    print(f"eval rate:            {eval_rate:.2f} (tokens/s)")


if __name__ == "__main__":
    messages = [("human", "Who are you?")]
    setup_ollama_llm(messages)
