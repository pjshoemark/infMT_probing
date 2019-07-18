import json, argparse, datetime




def process_dataset(counts_informal_filepath, counts_formal_filepath, distances_filepath, threshold_informal, threshold_formal, number_to_print):
	with open(counts_informal_filepath, 'r') as infile: 
		counts_informal = json.load(infile) 

	with open(counts_formal_filepath, 'r') as infile: 
		counts_formal = json.load(infile) 

	n = 0
	for line in list(reversed(list(open(distances_filepath, 'r')))): 
		try:
			(w,d) = line.strip().split('\t')
		except ValueError:
			d = line.strip().split('\t')
			w = ''
		if w in counts_informal:   
			count_informal = sum(counts_informal[w].values())
			top_informal = sorted(counts_informal[w].items(), key = lambda x:-x[1])[:3]
		else:
			count_informal = 0
			top_informal = 0
		if w in counts_formal:
			count_formal = sum(counts_formal[w].values())
			top_formal = sorted(counts_formal[w].items(), key = lambda x:-x[1])[:3]
		else:
			count_formal = 0
			top_formal = 0

		if count_informal >= threshold_informal and count_formal >= threshold_formal:
			n+= 1
			print('{}\nsource word: {}\nJS distance: {}\ncount in informal: {}\ncount in formal: {}\nmost aligned target words in informal:{}\nmost aligned target words in formal:{}\n\n'.format(n, w, d, count_informal, count_formal, top_informal, top_formal))
			

		if n == number_to_print:
			break





if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("-cm", "--counts_informal_filepath", type=str, help="path to file containing counts for informal corpus", default = 'europarl/en-ja/mtnt-trainclean-valid.en-ja.fa.lower.unigram_counts.json')
	parser.add_argument("-ce", "--counts_formal_filepath", type=str, help="path to file containing counts for formal corpus", default = 'europarl/en-ja/extra-trainclean-valid.en-ja.fa.lower.unigram_counts.json')
	parser.add_argument("-d", "--distances_filepath", type=str, help="path to file containing distances", default = 'europarl/en-ja/mtnt-trainclean-valid.en-ja.fa.lower.unigram_js_distances.d_05.tsv')
	parser.add_argument("-ti", "--threshold_informal", type=int, help="minimum count in informal", default = 200)
	parser.add_argument("-tf", "--threshold_formal", type=int, help="minimum count in formal", default = 0)
	parser.add_argument("-n", "--number_to_print", type=int, help="how many top-n results to show", default=10)   
	

	options = parser.parse_args()
	process_dataset(options.counts_informal_filepath, options.counts_formal_filepath, options.distances_filepath, options.threshold_informal, options.threshold_formal, options.number_to_print)
