from state import State

'''
sBest ← s0
bestCandidate ← s0
tabuList ← []
tabuList.push(s0)
while (not stoppingCondition())
	sNeighborhood ← getNeighbors(bestCandidate)
	for (sCandidate in sNeighborhood)
		if ( (not tabuList.contains(sCandidate)) and (fitness(sCandidate) > fitness(bestCandidate)) )
			bestCandidate ← sCandidate
		end
	end
	if (fitness(bestCandidate) > fitness(sBest))
		sBest ← bestCandidate
	end
	tabuList.push(bestCandidate)
	if (tabuList.size > maxTabuSize)
		tabuList.removeFirst()
	end
end
return sBest
'''


def TABU(initial_state: State, show_interim_results=True):
    if show_interim_results:
        print('The goal is to have two jars with 6 liters',
              'we use manhattan distance metrics and try to minimize it')
        print('Because we don\'t want to stay in local minimum, we always look for better candidates.')
        print('\nStart:\n\n')

    best_score = initial_state
    best_candidate = initial_state

    while not best_score.check_optimum():
        neighbours = best_candidate.get_possible_steps()

        best_candidate = neighbours[0]

        for neighbour in neighbours:
            if neighbour not in best_candidate.tabu_list and neighbour.metrics < best_candidate.metrics:
                best_candidate = neighbour

        if best_candidate.metrics < best_score.metrics:
            best_score = best_candidate
            best_score.tabu_list.append(best_score)

        if show_interim_results:
            print('Best score has {} with metrics={}\nBest candidate is {} with metrics={}\n\n'.format(
                best_score, best_score.metrics, best_candidate, best_candidate.metrics)
            )

    return best_score


if __name__ == '__main__':
    initial_state = State(data=(0, 0, 12))
    TABU(initial_state)
