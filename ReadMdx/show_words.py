# /bin/python3
import requests as rq
import sys
import re


from mdict_query import IndexBuilder
builder = IndexBuilder('mdx/bing.mdx')

dic = {}
sen = ''


def get_exp(word):
    result_text = builder.mdx_lookup(word)
    return result_text


def split_words(passage):
    l = re.split(r'[^a-zA-Z]', passage)
    n = set()
    for e in l:
        if e:
            n.add(e.lower())
    new_l = list(n)
    new_l.sort()
    return new_l


def split_sentences(passage):
    l = re.split(r'\. |? ', passage)
    return l


def main():
    words = split_words(sen)
    pairs = []
    for e in words:
        print("working on", e)
        exp = get_exp(e)
        if not exp:
            print("passed", e)
            continue
        if '中' not in exp[0]:
            pairs.append((exp[0],))
    with open("passage.html", "w") as f:
        f.write("<h1>文章原文</h1>")
        f.write(sen.replace("\n", "<br>"))        
        f.write('<h1>Total: %d words</h1>' % len(pairs))
        for e in pairs:
            f.write("<div style='margin: 5px 5px 5px 5px;'>%s</div>"%e)



if __name__ == "__main__":
    sen = '''
NARRATOR

Listen to part of a lecture in an environmental science class.

   
FEMALE PROFESSOR

Now, we've been talking about the loss of animal habitat from housing developments, um..., growing cities - small habitat losses.

   
But today I wanna begin talking about what happens when habitat is reduced across a large area.

   
There are, of course, animal species that require large areas of habitat, and some migrate over very long distances.

   
So what's the impact of habitat loss on those animals - animals that need large areas of habitat?

   
Well, I'll use the humming birds as an example.

   
Now you know a humming bird is amazingly small, but even though it's really tiny, it migrates over very long distances, travels up and down the western hemisphere - the Americas, back and forth between where it breeds in the summer and the warmer climates where it spends the winter.

   
So we would say that this whole area over which it migrates is its habitat because on this long-distance journey, it needs to come down to feed and sleep every so often, right?

   
Well, the humming bird beats its wings - get this - about 3 thousand times per minute.

   
So you think, wow, it must need a lot of energy, a lot of food, right?

   
Well, it does. It drinks a lot of nectar from flowers and feeds on some insects, but it's energy-efficient too.

   
You can't say it isn't. I mean, as it flies all the way across the Gulf of Mexico, it uses up almost none of its body fat.

   
But that doesn't mean it doesn't need to eat.

   
So humming birds have to rely on plants in their natural habitat.

   
And it goes without saying, but, well, the opposite is true as well, plants depend on humming birds too.

   
There are some flowers that can only be pollinated by the humming birds.

   
Without its stopping to feed and spreading pollen from flower to flower, these plants would cease to exist.

   
But the problem, well, as natural habitat along these migration routes is developed by humans for housing or agriculture or cleared for raising cattle, for instance, there is less food available for migrating humming birds.

   
Their nesting sites are affected too, the same, by the same sorts of human activities.

   
And all of these activities pose a real threat to the humming bird population.

   
So to help them survive, we need to preserve their habitats.

   
And one of the concrete ways people have been doing this is by cleaning up polluted habitat areas and then replanting flowers, um, replanting native flowers that humming birds feed on.

   
Promoting ecological tourism is another way to help save their habitat.

   
As the number of visitors, eco-tourists who come to humming bird habitats to watch the birds, the more the number of visitors grows, the more local businesses profit.

   
So ecological tourism can bring financial rewards, all the more reason to value these beautiful little creatures in their habitat, right?

   
But to understand more about how to protect and support humming birds the best we can, we've got to learn more about their breeding, nesting sites and migration routes, and also about the natural habitats we find there.

   
That should help us determine how to prevent further decline in the population.

   

A good research method, a good way to learn more, is by running a banding study.

   
Banding the birds allows us to track them over their lifetime. It's a practice that's been used by researchers for years.

   
In fact, most of what we've known about humming birds comes from banding studies, where we capture a humming bird and make sure all the information about it, like its weight and age and length, are all recorded, put into international, an international information database.

   
And then we place an extremely lightweight band on one of its legs, well, what looks like a leg, although technically it's considered part of the bird's foot.

   
Anyway, these bands are perfectly safe, and some humming birds have worn them for years with no evidence of any problems.

   
The band is labeled with a tracking number, oh, and there is a phone number on the band for people to call for free, to report a banded bird they've found or recaptured.

   

So when a banded bird is recaptured and reported, we learn about its migration route, its growth, and how long it has been alive, its life span.

   
One recaptured bird had been banded almost 12 years earlier - she is one of the oldest humming birds on record.

   

Another interesting thing we've learned is that some humming birds, um, they no longer use a certain route.

   
They travel by a different route to reach their destination.

   
And findings like these have been of interest to biologists and environmental scientists in a number of countries who are trying to understand the complexities of how changes in a habitat affect the species in it, species like the humming birds.
    '''
    main()
