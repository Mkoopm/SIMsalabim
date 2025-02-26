#!/bin/env python
from test_units.SIMsalabim import SIMsalabim
import warnings
from test_units.aux_functions import *

# ignore warnings for log of 0
warnings.filterwarnings("ignore", category=RuntimeWarning)


# Initialisation
test_idx = 0
SimSS = SIMsalabim(code_name='SimSS')
SimSS.compile_code()
ZimT = SIMsalabim(code_name='ZimT', work_dir='../ZimT')
ZimT.compile_code()
test_results = []

# Run test 1
test_idx += 1
x_sim = 'Vext'
y_sim = 'Jext'
x_test = 'Vext'
y_test = 'JSandH'
label_test = 'Sokel and Hughes'
plot_x = 'V$_{ext}$ [V]'
plot_y = 'J$_{ext}$ [A/m$^2$]'
log_x = True
log_y = True

labels = {'x' : plot_x, 'y' : plot_y}
dat_sim, dat_test = get_data_from_sim(SimSS, test_idx), get_data_from_file(test_idx, x_test, y_test)
rmse, dat_rmse = calc_selected_rmse(dat_sim, dat_test, log_x=log_x, log_y=log_y)
passed = rmse < 1e-4
test_results.append({'passed' : passed, 'test nr' : test_idx})
plot_test_results(test_idx, dat_sim, labels, dat_tests=[(label_test, dat_test)], dat_err=[(rmse, dat_rmse)], log_x=log_x, log_y=log_y)

# Run test 2
test_idx += 1
x_sim = 'Vext'
y_sim = 'Jext'
x_test = 'Vext'
y_test = 'Murgatroyd'
plot_x = 'V$_{ext}$ [V]'
plot_y = 'J$_{ext}$ [A/m$^2$]'

log_x = True
log_y = True

labels = {'x' : plot_x, 'y' : plot_y}
dat_sim, dat_test = get_data_from_sim(SimSS, test_idx), get_data_from_file(test_idx, x_test, y_test)
rmse, dat_rmse = calc_selected_rmse(dat_sim, dat_test, x_min=3, log_x=log_x, log_y=log_y)
passed = rmse < 6e-2
test_results.append({'passed' : passed, 'test nr' : test_idx})
plot_test_results(test_idx, dat_sim, labels, dat_tests=[(y_test, dat_test)], dat_err=[(rmse, dat_rmse)], log_x=log_x, log_y=log_y)


# Run test 3
test_idx += 1
x_sim = 'Vext'
y_sim = 'Jext'
x_test = 'Vext'
y_test = 'JRosenLampert'
label_test = 'Rosenberg and Lampert'
plot_x = 'V$_{ext}$ [V]'
plot_y = 'J$_{ext}$ [A/m$^2$]'
log_x = False
log_y = True

labels = {'x' : plot_x, 'y' : plot_y}
dat_sim, dat_test = get_data_from_sim(SimSS, test_idx), get_data_from_file(test_idx, x_test, y_test)
rmse, dat_rmse = calc_selected_rmse(dat_sim, dat_test, x_min=1.5, log_x=log_x, log_y=log_y)
passed = rmse < 1.3e-1
test_results.append({'passed' : passed, 'test nr' : test_idx})
plot_test_results(test_idx, dat_sim, labels, dat_tests=[(label_test, dat_test)], dat_err=[(rmse, dat_rmse)], log_x=log_x, log_y=log_y)


# Run test 4
test_idx += 1
x_sim = 'Vext'
y_sim = 'Jext'
x_test = 'Vext'
y_test = 'Jext'
y_ME = 'JME'
label_ME = 'Moving Electrode'
label_MG = 'Mott-Gurney'
y_MG = 'JMG'
plot_x = 'V$_{ext}$ [V]'
plot_y = 'J$_{ext}$ [A/m$^2$]'
log_x = True
log_y = True

labels = {'x' : plot_x, 'y' : plot_y}
dat_sim = get_data_from_sim(SimSS, test_idx)
dat_test_ME = get_data_from_file(test_idx, x_test, y_ME)
dat_test_MG = get_data_from_file(test_idx, x_test, y_MG)
dat_ME =  get_data_from_file(test_idx, x_test, y_ME)
dat_MG =  get_data_from_file(test_idx, x_test, y_MG)
dat_test_lst = [(label_ME, dat_test_ME), (label_MG, dat_test_MG)]
rmse_ME, dat_rmse_ME = calc_selected_rmse(dat_sim, dat_ME, x_max=0.2, log_x=log_x, log_y=log_y)
rmse_MG, dat_rmse_MG = calc_selected_rmse(dat_sim, dat_MG, x_min=4, log_x=log_x, log_y=log_y)
dat_err_lst = [(rmse_ME, dat_rmse_ME), (rmse_MG, dat_rmse_MG)]
passed = rmse_ME < 1.6e-2 and rmse_MG < 6e-2
test_results.append({'passed' : passed, 'test nr' : test_idx})
plot_test_results(test_idx, dat_sim, labels, dat_tests=dat_test_lst, dat_err=dat_err_lst, log_x=log_x, log_y=log_y)


# Run test 5
test_idx += 1
x_sim = 'Vext'
y_sim = 'Jext'
x_test = 'Vext'
y_test = 'JextREF'
label_test = 'No traps'
plot_x = 'V$_{ext}$ [V]'
plot_y = 'J$_{ext}$ [A/m$^2$]'
log_x = True
log_y = True

labels = {'x' : plot_x, 'y' : plot_y}
dat_sim, dat_test = get_data_from_sim(SimSS, test_idx), get_data_from_file(test_idx, x_test, y_test)
rmse_high, dat_rmse_high = calc_selected_rmse(dat_sim, dat_test, x_min=3.0, log_x=log_x, log_y=log_y)
rmse_low, dat_rmse_low = calc_selected_rmse(dat_sim, dat_test, x_max=0.1, log_x=log_x, log_y=log_y)
passed = rmse_high < 7e-2 and rmse_low > 0.5
test_results.append({'passed' : passed, 'test nr' : test_idx})
plot_test_results(test_idx, dat_sim, labels, dat_tests=[(label_test, dat_test)], dat_err=[(rmse_high, dat_rmse_high), (rmse_low, dat_rmse_low)], log_x=log_x, log_y=log_y)


# Run test 6
test_idx += 1
x_sim = 'Vext'
y_sim = 'Vext'
x_test = 'Gehp'
y_test = 'analytical'
label_test = 'Koster and Blom'
plot_x = 'G$_{ehp}$ [m$^{-3}$s$^{-1}$]'
plot_y = 'V$_{oc}$ [V]'
log_x = True
log_y = False

labels = {'x' : plot_x, 'y' : plot_y}
dat_sim, dat_test = get_data_from_sim(ZimT, test_idx, x=x_sim, y=y_sim, output_file='tj'), get_data_from_file(test_idx, x_test, y_test)
dat_sim = Data(dat_test.x, dat_sim.y)
rmse, dat_rmse = calc_selected_rmse(dat_sim, dat_test, log_x=log_x, log_y=log_y)
passed = rmse < 5.5e-4
test_results.append({'passed' : passed, 'test nr' : test_idx})
plot_test_results(test_idx, dat_sim, labels, dat_tests=[(label_test, dat_test)], dat_err=[(rmse, dat_rmse)], log_x=log_x, log_y=log_y)


# Run test 7
test_idx += 1
x_sim = 't'
y_sim = 'Jext'
fit_label = 'tau = {:.1e} s'
plot_x = 'time [s]'
plot_y = 'J$_{ext}$ [A/m$^2$]'
log_x = False
log_y = True

labels = {'x' : plot_x, 'y' : plot_y}
dat_sim = get_data_from_sim(ZimT, test_idx, x=x_sim, y=y_sim, output_file='tj')
RC_time, coeffs, dat_fit = fit_RC(dat_sim)
passed = abs(RC_time - 5e-6) < 0.5e-6

test_results.append({'passed' : passed, 'test nr' : test_idx})
plot_test_results(test_idx, dat_sim, labels, dat_tests=[(fit_label.format(RC_time), dat_fit)], log_x=log_x, log_y=log_y)


# Run test 8
test_idx = 8
x_sim = 't'
y_sim = 'Vext'
fit_label = 'tau = {:.1e} s'
guessed_fit_pars = [7e-6, 0.01, 1.5]
plot_x = 'V$_{oc}$ [V]'
plot_y = 'time [s]'
log_x = False
log_y = False

labels = {'x' : plot_x, 'y' : plot_y}
dat_sim = get_data_from_sim(ZimT, test_idx, x=x_sim, y=y_sim, output_file='tj')
#dat_sim = 
coeffs, dat_fit = fit_exp(dat_sim, guessed_fit_pars)
tau = coeffs[0]
passed = abs(tau - 7.09e-6) < 0.2e-6

test_results.append({'passed' : passed, 'test nr' : test_idx})
plot_test_results(test_idx, dat_sim, labels, dat_tests=[(fit_label.format(tau), dat_fit)], log_x=log_x, log_y=log_y)


# Run test 9
test_idx += 1
x_sim = 't'
y_sim = 'Jext'
fit_label = 'tau = {:.1e} s'
plot_x = 'time [s]'
plot_y = 'J$_{ext}$ [A/m$^2$]'
log_x = False
log_y = False

labels = {'x' : plot_x, 'y' : plot_y}
dat_sim = get_data_from_sim(ZimT, test_idx, x=x_sim, y=y_sim, output_file='tj')
dat_sim = Data(dat_sim.x[14:], dat_sim.y[14:])
coeffs, dat_fit = fit_exp(dat_sim)
tau = coeffs[0]
passed = abs(tau - 5e-2) < 0.01e-2

test_results.append({'passed' : passed, 'test nr' : test_idx})
plot_test_results(test_idx, dat_sim, labels, dat_tests=[(fit_label.format(tau), dat_fit)], log_x=log_x, log_y=log_y)


# Run test 10
test_idx += 1
x_sim = 't'
y_sim = 'Jext'
fit_label = 'tau = {:.1e} s'
plot_x = 'time [s]'
plot_y = 'J$_{ext}$ [A/m$^2$]'
log_x = False
log_y = False

labels = {'x' : plot_x, 'y' : plot_y}
dat_sim = get_data_from_sim(ZimT, test_idx, x=x_sim, y=y_sim, output_file='tj')
dat_sim = Data(dat_sim.x[14:], dat_sim.y[14:])
coeffs, dat_fit = fit_exp(dat_sim)
tau = coeffs[0]
passed = abs(tau - 2.5e-2) < 0.01e-2

test_results.append({'passed' : passed, 'test nr' : test_idx})
plot_test_results(test_idx, dat_sim, labels, dat_tests=[(fit_label.format(tau), dat_fit)], log_x=log_x, log_y=log_y)


# Print all results
print('\nResult:')
print_test_results(test_results)



