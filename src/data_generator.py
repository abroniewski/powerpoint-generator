import os
import datetime
import random
import csv


def create_students(num_students=100):
    disciplines = {
        "First Year": 23.11,
        "Mechanical Engineering": 21.28,
        "Electrical Engineering": 14.02,
        "Chemical Engineering": 12.47,
        "Civil Engineering": 10.70,
        "Software Engineering": 10.70,
        "Biomedical Engineering": 2,
        "Energy Engineering": 2,
        "Geomatics Engineering": 2,
        "Environmental Engineering": 2,
    }
    
    students = []
    
    for i in range(num_students):
        discipline = random.choices(list(disciplines.keys()), weights=disciplines.values())[0]
        
        if discipline == "First Year":
            year = 1
        else:
            year = random.randint(2, 5)
            year = random.choices([2, 3, 4, 5, 6], weights=[22, 20, 19, 16, 2])[0]
        
        # 80% of 4th and 5th-year students have internships
        if year in [4, 5]:
            internship = random.choices([1, 0], weights=[0.8, 0.2])[0]
        else:
            internship = 0

        # Pareto: 20% of students attend 80% of events
        attendance_likelihood = random.choices([0.8, 0.2], weights=[0.2, 0.8])[0]
        
        if year == 3:
            attendance_likelihood *= 1.3
        elif year == 4:
            attendance_likelihood *= 0.9
        elif year == 5:
            attendance_likelihood *= 1.2

        if random.random() < 0.05:
            attendance_likelihood += 0.3

        students.append({
            'student_id': i+1,
            'discipline': discipline,
            'year': year,
            'internship': internship,
            'attendance_likelihood': attendance_likelihood,
        })
        
    return students

def generate_event_data(event_id, students, num_tickets_sold, ticket_price, attendance_percentage):
    records = []

    # Sort the students based on attendance likelihood
    students_sorted_by_likelihood = sorted(students, key=lambda x: x['attendance_likelihood'], reverse=True)

    # Only consider the students who bought tickets
    students_with_tickets = students_sorted_by_likelihood[:num_tickets_sold]

    for student in students_with_tickets:
        # Decide if a student attended the event
        attended = "Yes" if random.random() < (student['attendance_likelihood'] * attendance_percentage / 100) else "No"

        records.append({
            'event_id': event_id,
            'student_id': student['student_id'],
            'ticket_price': ticket_price,
            'attended': attended,
            'discipline': student['discipline'],
            'year': student['year'],
            'internship': student['internship']
        })
    
    filename = f"event_data_{TIMESTAMP}.csv"
    filename = os.path.join('data', filename)

    # Check if the file exists
    mode = 'a' if os.path.exists(filename) else 'w'
    
    with open(filename, mode, newline='') as csvfile:
        fieldnames = ['event_id', 'student_id', 'ticket_price', 'attended', 'discipline', 'year', 'internship']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # Write the header only if the file doesn't exist (i.e., mode is 'w')
        if mode == 'w':
            writer.writeheader()

        for record in records:
            writer.writerow(record)


def generate_social_media_data(event_id, linkedin_posts, instagram_posts, email_ads):
    platforms = ["LinkedIn", "Instagram", "Email"]
    posts = []

    # Base metrics for posts on different platforms
    base_likes = {"LinkedIn": 15, "Instagram": 40, "Email": 100}
    base_shares = {"LinkedIn": 5, "Instagram": 15, "Email": 25}
    base_comments = {"LinkedIn": 3, "Instagram": 10, "Email": 10}

    for platform in platforms:
        if platform == "LinkedIn":
            num_posts = linkedin_posts
        elif platform == "Instagram":
            num_posts = instagram_posts
        else:  # Email
            num_posts = email_ads

        for i in range(num_posts):
            post_id = len(posts) + 1
            
            # Occasionally introduce an outlier for days_before_event
            if random.random() < 0.05:  # 5% chance for an outlier
                days_before_event = random.choice([90, 120])
            else:
                days_before_event = random.choice([60, 45, 30, 15, 7, 3, 1])

            # Base engagement metrics
            likes = random.randint(base_likes[platform] - 5, base_likes[platform] + 15)
            shares = random.randint(base_shares[platform] - 2, base_shares[platform] + 5)
            comments_replies = random.randint(base_comments[platform] - 1, base_comments[platform] + 7)

            # Occasionally introduce outliers in engagement metrics
            outlier_chance = random.random()
            if outlier_chance < 0.05:  # 5% chance for significantly higher engagement
                likes += random.randint(100, 300)
                shares += random.randint(20, 50)
                comments_replies += random.randint(20, 40)
            elif 0.05 <= outlier_chance < 0.10:  # 5% chance for significantly lower engagement
                likes = max(0, likes - random.randint(5, 10))
                shares = max(0, shares - random.randint(2, 5))
                comments_replies = max(0, comments_replies - random.randint(2, 7))

            posts.append({
                'event_id': event_id,
                'post_id': post_id,
                'platform': platform,
                'days_before_event': days_before_event,
                'likes': likes,
                'shares': shares,
                'comments_replies': comments_replies
            })


    filename = f"social_media_data_{TIMESTAMP}.csv"
    filename = os.path.join('data', filename)
    # Check if the file exists
    mode = 'a' if os.path.exists(filename) else 'w'
    
    with open(filename, mode, newline='') as csvfile:
        fieldnames = ['event_id', 'post_id', 'platform', 'days_before_event', 'likes', 'shares', 'comments_replies']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # Write the header only if the file doesn't exist (i.e., mode is 'w')
        if mode == 'w':
            writer.writeheader()

        for post in posts:
            writer.writerow(post)


def generate_professional_data(event_id, ticket_price, total_sponsorship, num_sponsors, num_companies_attending):
    companies = ["Company A", "Company B", "Company C", "Company D", "Company E",
                 "Company F", "Company G", "Company H", "Company I", "Company J",
                 "Company K", "Company L", "Company M", "Company N", "Company O"]
    
    data = []
    
    # Randomly select companies that are attending
    attending_companies = random.sample(companies, num_companies_attending)
    
    # Randomly select companies from attending companies to be sponsors
    sponsoring_companies = random.sample(attending_companies, num_sponsors)
    
    # Distribute total_sponsorship in a tiered manner
    tiers = ['low', 'medium', 'high']
    tier_values = {'low': [500, 1000], 'medium': [1500, 2000], 'high': [2500, 3000]}
    
    sponsorship_allocated = 0
    for company in sponsoring_companies:
        tier = random.choice(tiers)
        sponsorship = random.randint(tier_values[tier][0], tier_values[tier][1])
        if sponsorship_allocated + sponsorship <= total_sponsorship:
            sponsorship_allocated += sponsorship
        else:
            sponsorship = total_sponsorship - sponsorship_allocated  # Remaining amount
            sponsorship_allocated = total_sponsorship

        data.append({
            'event_id': event_id,
            'company_name': company,
            'ticket_price': ticket_price,
            'attendees': random.randint(1, 5),
            'sponsorship_amount': sponsorship
        })
        
    # Add attending companies that are not sponsors with 0 sponsorship amount
    for company in attending_companies:
        if company not in sponsoring_companies:
            data.append({
                'event_id': event_id,
                'company_name': company,
                'ticket_price': ticket_price,
                'attendees': random.randint(1, 5),
                'sponsorship_amount': 0
            })
        
    filename = f"professional_data_{TIMESTAMP}.csv"
    filename = os.path.join('data', filename)

    # Check if the file exists
    mode = 'a' if os.path.exists(filename) else 'w'
    
    with open(filename, mode, newline='') as csvfile:
        fieldnames = ['event_id', 'company_name', 'ticket_price', 'attendees', 'sponsorship_amount']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # Write the header only if the file doesn't exist (i.e., mode is 'w')
        if mode == 'w':
            writer.writeheader()
        
        for record in data:
            writer.writerow(record)


# Global timestamp for all CSVs
TIMESTAMP = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

def main():


    # Create a directory for the data files if it doesn't exist
    if not os.path.exists('data'):
        os.makedirs('data')

    # Generate 175 students
    students = create_students(175)

    # For Event 1
    event_id = 1
    generate_event_data(event_id, students, num_tickets_sold=150, ticket_price=0, attendance_percentage=60)
    generate_social_media_data(event_id, linkedin_posts=3, instagram_posts=5, email_ads=4)
    generate_professional_data(event_id, ticket_price=0, total_sponsorship=5000, num_sponsors=5, num_companies_attending=10)

    # For Event 2
    event_id = 2
    generate_event_data(event_id, students, num_tickets_sold=20, ticket_price=10, attendance_percentage=95)
    generate_social_media_data(event_id, linkedin_posts=3, instagram_posts=5, email_ads=4)
    generate_professional_data(event_id, ticket_price=10, total_sponsorship=2000, num_sponsors=3, num_companies_attending=7)

    # For Event 3
    event_id = 3
    generate_event_data(event_id, students, num_tickets_sold=50, ticket_price=10, attendance_percentage=85)
    generate_social_media_data(event_id, linkedin_posts=3, instagram_posts=5, email_ads=4)
    generate_professional_data(event_id, ticket_price=10, total_sponsorship=3000, num_sponsors=4, num_companies_attending=8)


if __name__ == '__main__':
    main()