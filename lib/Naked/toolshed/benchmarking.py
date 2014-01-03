#!/usr/bin/env python

import sys
import time
from functools import wraps

#------------------------------------------------------------------------------
# [ timer function decorator ]
#  runs timed repetitions of the decorated function in a single trial
#  default is 100,000 repetitions in the trial
#  reports the results of the trial
#  Usage example:
#   	from Naked.toolshed.benchmarking import timer
#		@timer
#		def myfunction():
#------------------------------------------------------------------------------
def timer(func, repetitions=100000):
	@wraps(func)
	def wrapper(*args, **kwargs):
		sys.stdout.write("Starting " + str(repetitions) + " repetitions of " + func.__name__ + "()...")
		sys.stdout.flush()
		print(" ")
		start = time.time()
		for x in range(repetitions):
			result = func(*args, **kwargs)
		end = time.time()
		print(str(repetitions) + " repetitions of " + func.__name__ + " : " + str(end-start) + " sec")
		return result
	return wrapper

#------------------------------------------------------------------------------
# [ timer_X function decorators ]
#   replicate the above decorator with different number of repetitions
#------------------------------------------------------------------------------

def timer_10(func, repetitions=10):
	@wraps(func)
	def wrapper(*args, **kwargs):
		sys.stdout.write("Starting " + str(repetitions) + " repetitions of " + func.__name__ + "()...")
		sys.stdout.flush()
		print(" ")
		start = time.time()
		for x in range(repetitions):
			result = func(*args, **kwargs)
		end = time.time()
		print(str(repetitions) + " repetitions of " + func.__name__ + " : " + str(end-start) + " sec")
		return result
	return wrapper

def timer_100(func, repetitions=100):
	@wraps(func)
	def wrapper(*args, **kwargs):
		sys.stdout.write("Starting " + str(repetitions) + " repetitions of " + func.__name__ + "()...")
		sys.stdout.flush()
		print(" ")
		start = time.time()
		for x in range(repetitions):
			result = func(*args, **kwargs)
		end = time.time()
		print(str(repetitions) + " repetitions of " + func.__name__ + " : " + str(end-start) + " sec")
		return result
	return wrapper

def timer_1k(func, repetitions=1000):
	@wraps(func)
	def wrapper(*args, **kwargs):
		sys.stdout.write("Starting " + str(repetitions) + " repetitions of " + func.__name__ + "()...")
		sys.stdout.flush()
		print(" ")
		start = time.time()
		for x in range(repetitions):
			result = func(*args, **kwargs)
		end = time.time()
		print(str(repetitions) + " repetitions of " + func.__name__ + " : " + str(end-start) + " sec")
		return result
	return wrapper

def timer_10k(func, repetitions=10000):
	@wraps(func)
	def wrapper(*args, **kwargs):
		sys.stdout.write("Starting " + str(repetitions) + " repetitions of " + func.__name__ + "()...")
		sys.stdout.flush()
		print(" ")
		start = time.time()
		for x in range(repetitions):
			result = func(*args, **kwargs)
		end = time.time()
		print(str(repetitions) + " repetitions of " + func.__name__ + " : " + str(end-start) + " sec")
		return result
	return wrapper

def timer_1m(func, repetitions=1000000):
	@wraps(func)
	def wrapper(*args, **kwargs):
		sys.stdout.write("Starting " + str(repetitions) + " repetitions of " + func.__name__ + "()...")
		sys.stdout.flush()
		print(" ")
		start = time.time()
		for x in range(repetitions):
			result = func(*args, **kwargs)
		end = time.time()
		print(str(repetitions) + " repetitions of " + func.__name__ + " : " + str(end-start) + " sec")
		return result
	return wrapper

#------------------------------------------------------------------------------
# [ timer_trials function decorator ]
#  runs a series of timed trials with the decorated function
#  default is 10 trials x 100,000 repetitions per trial
#  reports each of the trial results and the mean across all trials
#  Usage example:
#   	from Naked.toolshed.benchmarking import timer_trials
#		@timer_trials
#		def myfunction():
#------------------------------------------------------------------------------
def timer_trials(func, repetitions=100000, trials=10):
	@wraps(func)
	def wrapper(*args, **kwargs):
		sys.stdout.write("Starting timed trials of " + func.__name__ + "()")
		sys.stdout.flush()
		result_list = []
		for x in range(trials):
			start = time.time()
			for y in range(repetitions):
				result = func(*args, **kwargs)
			end = time.time()
			result_list.append(end-start)
			sys.stdout.write(".")
			sys.stdout.flush()
		print(" ")
		n = 1
		for run in result_list:
			print("Trial " + str(n) + ":\t" + str(run))
			n += 1
		print("-"*50)
		mean = sum(result_list)/len(result_list)
		print("Mean for " + str(repetitions) + " repetitions: " + str(mean) + " sec")
		print("Mean per repetition: " + str(mean/repetitions) + " sec")
		return result
	return wrapper

#------------------------------------------------------------------------------
# [ timer_trials_X ]
#  replicate the above decorator with a different number of repetitions x 10 trials
#------------------------------------------------------------------------------

def timer_trials_10(func, repetitions=10, trials=10):
	@wraps(func)
	def wrapper(*args, **kwargs):
		sys.stdout.write("Starting timed trials of " + func.__name__ + "()")
		sys.stdout.flush()
		result_list = []
		for x in range(trials):
			start = time.time()
			for y in range(repetitions):
				result = func(*args, **kwargs)
			end = time.time()
			result_list.append(end-start)
			sys.stdout.write(".")
			sys.stdout.flush()
		print(" ")
		n = 1
		for run in result_list:
			print("Trial " + str(n) + ":\t" + str(run))
			n += 1
		print("-"*50)
		mean = sum(result_list)/len(result_list)
		print("Mean for " + str(repetitions) + " repetitions: " + str(mean) + " sec")
		print("Mean per repetition: " + str(mean/repetitions) + " sec")
		return result
	return wrapper

def timer_trials_100(func, repetitions=100, trials=10):
	@wraps(func)
	def wrapper(*args, **kwargs):
		sys.stdout.write("Starting timed trials of " + func.__name__ + "()")
		sys.stdout.flush()
		result_list = []
		for x in range(trials):
			start = time.time()
			for y in range(repetitions):
				result = func(*args, **kwargs)
			end = time.time()
			result_list.append(end-start)
			sys.stdout.write(".")
			sys.stdout.flush()
		print(" ")
		n = 1
		for run in result_list:
			print("Trial " + str(n) + ":\t" + str(run))
			n += 1
		print("-"*50)
		mean = sum(result_list)/len(result_list)
		print("Mean for " + str(repetitions) + " repetitions: " + str(mean) + " sec")
		print("Mean per repetition: " + str(mean/repetitions) + " sec")
		return result
	return wrapper

def timer_trials_1k(func, repetitions=1000, trials=10):
	@wraps(func)
	def wrapper(*args, **kwargs):
		sys.stdout.write("Starting timed trials of " + func.__name__ + "()")
		sys.stdout.flush()
		result_list = []
		for x in range(trials):
			start = time.time()
			for y in range(repetitions):
				result = func(*args, **kwargs)
			end = time.time()
			result_list.append(end-start)
			sys.stdout.write(".")
			sys.stdout.flush()
		print(" ")
		n = 1
		for run in result_list:
			print("Trial " + str(n) + ":\t" + str(run))
			n += 1
		print("-"*50)
		mean = sum(result_list)/len(result_list)
		print("Mean for " + str(repetitions) + " repetitions: " + str(mean) + " sec")
		print("Mean per repetition: " + str(mean/repetitions) + " sec")
		return result
	return wrapper

def timer_trials_10k(func, repetitions=10000, trials=10):
	@wraps(func)
	def wrapper(*args, **kwargs):
		sys.stdout.write("Starting timed trials of " + func.__name__ + "()")
		sys.stdout.flush()
		result_list = []
		for x in range(trials):
			start = time.time()
			for y in range(repetitions):
				result = func(*args, **kwargs)
			end = time.time()
			result_list.append(end-start)
			sys.stdout.write(".")
			sys.stdout.flush()
		print(" ")
		n = 1
		for run in result_list:
			print("Trial " + str(n) + ":\t" + str(run))
			n += 1
		print("-"*50)
		mean = sum(result_list)/len(result_list)
		print("Mean for " + str(repetitions) + " repetitions: " + str(mean) + " sec")
		print("Mean per repetition: " + str(mean/repetitions) + " sec")
		return result
	return wrapper

def timer_trials_1m(func, repetitions=1000000, trials=10):
	@wraps(func)
	def wrapper(*args, **kwargs):
		sys.stdout.write("Starting timed trials of " + func.__name__ + "()")
		sys.stdout.flush()
		result_list = []
		for x in range(trials):
			start = time.time()
			for y in range(repetitions):
				result = func(*args, **kwargs)
			end = time.time()
			result_list.append(end-start)
			sys.stdout.write(".")
			sys.stdout.flush()
		print(" ")
		n = 1
		for run in result_list:
			print("Trial " + str(n) + ":\t" + str(run))
			n += 1
		print("-"*50)
		mean = sum(result_list)/len(result_list)
		print("Mean for " + str(repetitions) + " repetitions: " + str(mean) + " sec")
		print("Mean per repetition: " + str(mean/repetitions) + " sec")
		return result
	return wrapper

if __name__ == '__main__':
	pass
