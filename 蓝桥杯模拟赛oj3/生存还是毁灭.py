str = ''' To be, or not to be: that is the question,
Whether it's nobler in the mind to suffer
The slings and arrows of outrageous fortune,
Or to take arms against a sea of troubles,
And by opposing end them. To die,to sleep;
No more; and by a sleep to say we end
The heartache, and the thousand natural shocks
That flesh is heir to, it's a consummation
Devoutly to be wished. To die, to sleep.
To sleep, perchance to dream: ay, there's the rub;
For in that sleep of death what dreams may come
When we have shuffled off this mortal coil,
Must give us pause. There's the respect
That makes calamity of so long life;
For who would bear the whips and scorns of time,
The oppressor's wrong, the proud man's contumely,
The pangs of despised love, the law's delay,
The insolence of office, and the spurns
That patient merit of the unworthy takes,
When he himself might his quietus make
With a bare bodkin? Who would fardels bear,
To grunt and sweat under a weary life,
But that the dread of something after death,
The undiscovered country from whose bourn
No traveller returns, puzzles the will,
And makes us rather bear those ills we have
Than fly to others that we know not of?
Thus conscience does make cowards of us all,
And thus the native hue of resolution
Is sicklied or with the pale cast of thought,
And enterprises of great pith and moment
With this regard their currents turn awry
And lose the name of action.'''
strq = ""
tmp = 0
ans = 0
# 97 122 65 90
for i in str:
    if 65<=ord(i)<=90 or 97<=ord(i)<=122:
        strq += i.lower()
for i in strq:
    tmp = strq.count(i)
    if tmp>ans:
        ans = tmp
print(ans)