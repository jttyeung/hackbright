
// Learning how to write scripts in javascript.

var melonsToAdd = ['Ogen', 'Horned Melon', 'Watermelon', 'Casaba',
                     'Sharlyn', 'Xigua', 'Ogen', 'Christmas', 'Christmas',
                     'Christmas', 'Christmas', 'Watermelon', 'Sharlyn', 'Xigua',
                     'Cantaloupe', 'Christmas', 'Watermelon', 'Christmas',
                     'Sharlyn', 'Christmas', 'Cantaloupe', 'Casaba', 'Cantaloupe',
                     'Santa Claus', 'Horned Melon', 'Watermelon', 'Ogen',
                     'Horned Melon', 'Cantaloupe', 'Xigua', 'Horned Melon', 'Sharlyn',
                     'Horned Melon', 'Sharlyn', 'Cantaloupe', 'Christmas',
                     'Horned Melon', 'Horned Melon', 'Horned Melon', 'Xigua', 'Xigua',
                     'Watermelon', 'Cantaloupe', 'Casaba', 'Cantaloupe', 'Casaba',
                     'Watermelon', 'Santa Claus', 'Casaba'];


function countMelons(melonsArray){

    var melonCounts = {};
    var melon;


    for (var i = 0; i < melonsArray.length; i++){
        melon = melonsArray[i];
        // melonCounts[melon] = melonCounts[melon] || 0;
        if (melon in melonCounts){
            melonCounts[melon]++;
        }
        else{
            melonCounts[melon] = 1;
        }

    }

    console.log(melonCounts);

    return melonCounts;

}

countMelons(melonsToAdd);
