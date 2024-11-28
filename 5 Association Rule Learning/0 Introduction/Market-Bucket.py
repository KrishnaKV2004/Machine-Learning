'''
    Transaction ID	           Items
    
          1	          |        {Bread, Milk}
          2	          |        {Bread, Diaper, Beer}
          3	          |        {Milk, Diaper, Beer, Cola}
          4	          |        {Bread, Milk, Diaper, Beer}
          5	          |        {Bread, Milk, Cola}
          
    Our goal is to find association rules between these items based on support and confidence.
    
    Steps :
    
    Support of an itemset (e.g., {Bread}) is the proportion of transactions that contain that itemset.
    Confidence of a rule (e.g., {Bread} -> {Milk}) is the proportion of transactions containing
    {Bread} that also contain {Milk}.
    
    Approach :

    We'll calculate the support of itemsets and use this to generate association rules.
    We'll then compute the confidence of those rules.
    We'll consider a simple rule: {X} → {Y}, where X and Y are itemsets.
'''

#   Importing Libraries -->

from itertools import combinations

#   Transactions Dataset -->

transactions = [
    {"Bread", "Milk"},
    {"Bread", "Diaper", "Beer"},
    {"Milk", "Diaper", "Beer", "Cola"},
    {"Bread", "Milk", "Diaper", "Beer"},
    {"Bread", "Milk", "Cola"}
]

#   Function To Calculate Support Of Itemset -->

def calculate_support(itemset, transactions):
    count = 0
    for transaction in transactions:
        if itemset.issubset(transaction):
            count += 1
    return count / len(transactions)

#   Function To Calculate Confidence Of A Rule -->

def calculate_confidence(rule, transactions):
    antecedent, consequent = rule
    support_antecedent = calculate_support(antecedent, transactions)
    support_rule = calculate_support(antecedent.union(consequent), transactions)
    return support_rule / support_antecedent if support_antecedent > 0 else 0

#   Generate All possible 1-itemsets, 2-itemsets, etc.

itemsets = set()
for transaction in transactions:
    for item in transaction:
        itemsets.add(frozenset([item]))
        
#   Generating All Possible Pairs (2-itemsets) And Checking For Rules -->

rules = []
for itemset_size in range(2, len(itemsets)+1):  # Start from 2-itemsets
    for itemset in combinations(itemsets, itemset_size):
        itemset = frozenset(itemset)  # Converting to a frozenset
        
        # Generate All Possible Splits Of Itemset Into Antecedent and Consequent -->
        
        for antecedent_size in range(1, len(itemset)):
            for antecedent in combinations(itemset, antecedent_size):
                antecedent = frozenset(antecedent)
                consequent = itemset - antecedent
                confidence = calculate_confidence((antecedent, consequent), transactions)
                if confidence > 0.5:  # Minimum confidence threshold
                    rules.append((antecedent, consequent, confidence))
                    
# Display The Rules With Confidence > 0.5 -->

for rule in rules:
    antecedent, consequent, confidence = rule
    print(f"Rule: {set(antecedent)} → {set(consequent)} | Confidence: {confidence:.2f}")
    
    
'''
    Explanation -->
    
    Support measures how frequently an itemset appears in the dataset.
    Confidence measures the likelihood of one item appearing in a transaction
    when another item is present.
    This example generates itemsets, splits them into antecedents and consequents,
    and calculates their confidence, finally filtering out the ones with a confidence less than 0.5.
    This approach is simple and doesn't rely on complex algorithms like Apriori or FP-Growth
    but works for small datasets. For larger datasets, using optimized algorithms like Apriori
    or FP-Growth is more efficient.
'''