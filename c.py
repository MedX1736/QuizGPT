import csv

def extract_questions_and_responses(file_path):
    questions = []
    answers = []
    answer = None
    with open(file_path, 'r' , encoding="utf8") as file:
        lines = file.readlines()
        
        for i in range(0,len(lines)) :
            line = lines[i].strip()
            if line.startswith("Question :"):
                question = line.replace("Question :", "").strip()
                questions.append(question)
                if answer : 
                    answers.append(answer)
            elif line.startswith("Réponse :"):
                answer = line.replace("Réponse :", "").strip()
            else :
                answer += line.strip() + '\n'
    return questions, answers

def write_to_csv(file_path, questions, responses):
    with open(file_path, 'w', newline='', encoding="utf8") as file:
        writer = csv.writer(file)
        writer.writerow(['Question', 'Response'])  # Write header
        
        for question, response in zip(questions, responses):
            writer.writerow([question, response])

# Usage example
file_path = "generated_questions/TPRO/questions.txt"  # Replace with the path to your file
output_csv_path = 'output.csv'  # Path to the output CSV file

questions, responses = extract_questions_and_responses(file_path)
write_to_csv(output_csv_path, questions, responses)