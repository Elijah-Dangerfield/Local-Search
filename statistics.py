import numpy

def main():
    sim_an = numpy.loadtxt('sa_stats.txt')
    greedy = numpy.loadtxt('greedy_stats.txt')

    sa_count = 0.0
    sa_outperformance = 0.0
    sa_best = 0.0


    greedy_count = 0.0
    greed_outperformance = 0.0
    greedy_best = 0.0

    for i in range(len(greedy)):
        if sim_an[i] - greedy[i] >= 1e-8:
            sa_count += 1
            result = sim_an[i] - greedy[i]
            sa_outperformance += result
            if result > sa_best:
                sa_best = result

        elif greedy[i] - sim_an[i] >= 1e-8:
            greedy_count += 1
            result = greedy[i] - sim_an[i]
            greed_outperformance += result
            if result > greedy_best:
                greedy_best = result


    print("Simulated Annealing out performed Greedy Hill Climbing on ", sa_count, " runs")
    print("when sa out performed it found a better maxima by an average of ", sa_outperformance / sa_count, )
    print("The greatest out performance of Simulated Annealing that Greedy did was ", sa_best)
    print('\n\n')
    print("Greedy out performed Simulated Annealing on ", greedy_count, " runs")
    print("when greedy out performed it found a better maxima by an average of ", greed_outperformance / greedy_count,)
    print("The greatest out performance of Simulated Annealing that Greedy did was ", greedy_best )







if __name__ == '__main__':
    main()