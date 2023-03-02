import os
import openai

openai.api_key = os.getenv('OPENAI_API_KEY')


def gpt_req_res(subject_text='write an essay on any subject.',
                prompt_base='answer like an experienced consultant: ',
                model='text-davinci-003',
                max_tokens=1200,
                temperature=0.8):

    # https://platform.openai.com/docs/api-reference/completions/create
    response = openai.Completion.create(
        model=model,
        prompt=prompt_base + ': ' + subject_text,
        temperature=temperature,
        max_tokens=1200,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    return response.choices[0].text


if __name__ == '__main__':
    text = 'help your client find their why'
    prompt = 'act like simon sinek: '
    reply = gpt_req_res(text, prompt)
    # print(reply)
    print(reply)
