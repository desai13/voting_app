from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

"""
# 3 Month Review

_“Life can only be understood backwards; but it must be lived forwards.”
― **Søren Kierkegaard**_

After appreciating the opportunity to reflect on the last three months at work, I thought it might be useful to do a 
similar exercise but for broader aspects of my life. The work review had the effect of aligning me to the company's 
goals, whereas doing one for myself could perhaps let me retrospectively work out the areas in my where I'm making
progress, and highlight areas where I might have drifted away from what I'd want for/from myself.

I think I will split this in to two sections big sections: work and relationships. I think these categories are broad
enough to encapsulate anything I'd like to reflect on.

## Work
### How have you felt about work over the last 3 months?

_**TLDR**: Enjoying work,  learning a lot and working with talented and pleasant people. Dealing with typical anxieties of
starting a new role, but feeling them ease over time._

I like my job. I remember feeling elements of excited and nervous when I was joining at the end of Jan (I'm sure no one
else has ever felt those emotions when starting a new job lol). However, underlying it there was also a certain level
of confidence which I didn't have in my first job. Cominging in with experience, despite being only a year, meant it was
more natural to get assimilated into a working rhythm. I still remember being quite stressed for the first couple of
weeks when I was getting my VM set up because it was novel and also quite out of my control at the pace it happens - 
there is lots of security around everything, which meant everytime I wanted access to a database, permission to view
certain Jira/Confluence pages, or intall anything on my VM I need to request permission from Gabe (group lead) and then
wait till someone from the IT team got to my ticket. When all this finally got sorted out and I everything available
to me that I needed to do my work I felt a lot more settled.

The meetings and work generally had a steep learning curve (I've not worked properly with logistic regression models
before so had to read into a lot of new stuff - also had to learn how to use MATLAB/SQL). This was confounded by the
somewhat absurd amount of terminology you get with sports too - if someone mentions a maiden in a meeting do they mean
a cricket over with no runs scored, a horse that has never won a race, or an unmarried woman?

Despite the learning curve, I felt I was put at ease by people like Charlie (my manager) and Jules (runs horse racing)
who spoke to me about how overwhelming everything was when they started. I was also put at ease because I was surrounded
by members with a similar education background to me i.e. generally science more research/maths focussed than coding. I 
also noticed that perhaps studying at Oxford provided me with another layer or validation and reassurance that I was at
the level required. On reflection, there are several components to what make me feel at ease in my job - my education, 
my experience (1 prior year as a data-scientist), the fact that I'd been judged in an interview, and my belief in my 
ability. Ideally it would be just be the latter that I could rely on, but in moments of self-doubt and anxiety, I do
find myself falling back on the other three. Even still, I do get periods where they're not enough, e.g. Oxford
shouldn't have accepted me, these guys misjudged me at the interview, I'm going to say something so stupid that
they realise and fire me, etc. I think when I'm anxious I need tangible evidence rather than something vague and
vacillatory like "self-belief" - which makes me hopeful, because as time passes there will be more evidence that I can 
call to mind when these anxious thoughts begin.

### What are you looking to get out of the next 3 months?
I'm looking to build stronger relationships with more people. I've got comfortable with Charlie, but not really with
anyone else. My kind of work makes it a bit tricky to spend time with people, which means I need to work on being
more proactive. I'm going to go into the office more often, and also make more of an effort throughout the work day
to get coffee with people. I think I'll rarely make an effort to socialise after work however, as due to the commute
I'm always keen to leave as soon as I'm done for the day.

I'd also like to build a stronger idea of the direction I'd like to go within the company regarding my work. Up till
now I've worked exclusively on horse-racing, and have really enjoyed my projects. I want to spend some time working on
sports, particularly football, due to my general sporting interest; however, I think from a data science perspective 
I'm much more drawn towards horse racing due to there being such a rich dataset, and the fact that most of the simple
stuff that can be done has been so there is a drive to come up with more interesting and complex ideas/methodologies.

## Relationships
### Family

### Friends

### Links








"""

with st.echo(code_location='below'):
    total_points = st.slider("Number of points in spiral", 1, 5000, 2000)
    num_turns = st.slider("Number of turns in spiral", 1, 100, 9)

    Point = namedtuple('Point', 'x y')
    data = []

    points_per_turn = total_points / num_turns

    for curr_point_num in range(total_points):
        curr_turn, i = divmod(curr_point_num, points_per_turn)
        angle = (curr_turn + 1) * 2 * math.pi * i / points_per_turn
        radius = curr_point_num / total_points
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        data.append(Point(x, y))

    st.altair_chart(alt.Chart(pd.DataFrame(data), height=500, width=500)
        .mark_circle(color='#0068c9', opacity=0.5)
        .encode(x='x:Q', y='y:Q'))