import numpy as np

if __name__ == '__main__':
    papers = np.load('Conferences/ICLR2024.npz', allow_pickle=True)['papers']

    words = ['CKA']#Put the key works here. For example, words = ['CKA', 'similarity']
    words = [x.lower() for x in words]

    th = 10#Frequency of keywords throughout the text.
    for paper in papers:
        file, content = paper[0], paper[1]
        hit = 0
        for word in words:
            if word in content.keys():
                if content[word] >= th:
                    hit = hit + 1

        if hit >= len(words):
            print(file)

