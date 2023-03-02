from m02_read_pdf_text import get_pdf_text
from m01_gpt3_req import gpt_req_res

if __name__ == '__main__':
    doc_path_name = 'documents/chat_gpt_ubs.pdf'
    doc_text = get_pdf_text(doc_path_name, 1, 2)
    # print(doc_text)
    prompt = 'summarize like an experienced consultant in 5 bullets: '
    reply = gpt_req_res(doc_text, prompt)
    print(reply)
