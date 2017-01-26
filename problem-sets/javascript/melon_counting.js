melonsToAdd = ['Ogen', 'Horned Melon', 'Watermelon', 'Casaba',
                'Sharlyn', 'Xigua', 'Ogen', 'Christmas', 'Christmas',
                'Christmas', 'Christmas', 'Watermelon', 'Sharlyn', 'Xigua',
                'Cantaloupe', 'Christmas', 'Watermelon', 'Christmas',
                'Sharlyn', 'Christmas', 'Cantaloupe', 'Casaba', 'Cantaloupe',
                'Santa Claus', 'Horned Melon', 'Watermelon', 'Ogen',
                'Horned Melon', 'Cantaloupe', 'Xigua', 'Horned Melon', 'Sharlyn',
                'Horned Melon', 'Sharlyn', 'Cantaloupe', 'Christmas',
                'Horned Melon', 'Horned Melon', 'Horned Melon', 'Xigua', 'Xigua',
                'Watermelon', 'Cantaloupe', 'Casaba', 'Cantaloupe', 'Casaba',
                'Watermelon', 'Santa Claus', 'Casaba']


var count_melons = function(melonList) {
    var melonCounts = {};

    for (var i = 0; i < melonList.length; i++) {
        melon = melonsToAdd[i]
        if (melon in melonCounts) {
            melonCounts[melon]++;
        }
        else {
            melonCounts[melon] = 1;
        }
    }

    return melonCounts;
};

count_melons(melonsToAdd)
