import csv

def extract_questions_and_responses(file_path):
    questions = []
    answers = []
    answer = None
    qst = 0 
    with open(file_path, 'r' , encoding="utf8") as file:
        lines = file.readlines()
        i=0
        while i < len(lines)-1 :
            line = lines[i].strip()
            if line.startswith("Réponse :"):
                answer = line.replace("Réponse :", "").strip()
                for j in range(i,len(lines)):
                    if (lines[i+1].startswith("Question :")) or (lines[i+1].startswith("Q :")) :
                        answers.append(answer)
                        answer= ""
                        break;
                    else : 
                        answer += lines[i+1].strip() + '\n'
                        i = i +1
            elif line == "":
                continue 
            else:
                if (line.startswith("Question :")):
                    question = line.replace("Question :", "").strip() + '\n'
                if (line.startswith("Q :")):
                    question = line.replace("Q :", "").strip() + '\n'
                for j in range(i,len(lines)):
                    if lines[i+1].startswith("Réponse :") :
                        questions.append(question)
                        question =""
                        break
                    else :
                        question += lines[i+1].strip() + '\n'
                        i = i +1
            i = i+1
            
    return questions, answers

def write_to_csv(file_path, questions, responses):
    with open(file_path, 'w', newline='', encoding="utf8") as file:
        writer = csv.writer(file)
        writer.writerow(['Question', 'Response'])  # Write header
        
        for question, response in zip(questions, responses):
            writer.writerow([question, response])

# Usage example
file_path = "generated_questions/TPRO/quizs.txt"  # Replace with the path to your file
output_csv_path = 'quiz.csv'  # Path to the output CSV file

questions, responses = extract_questions_and_responses(file_path)
write_to_csv(output_csv_path, questions, responses)