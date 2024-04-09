
signal_values = [1, 2, 3, 4, 5];


time_interval = 1;


integral_result = trapz(signal_values) * time_interval;


disp(['The integrated value of the signal is: ', num2str(integral_result)]);

