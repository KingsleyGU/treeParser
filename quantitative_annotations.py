	#################
	# Quantitative Annotations #
	#################
qa = {
	r'(MAKE Fred Charlie MOVE Charlie LOCATION door door)':
	'<node refinement="disjunctive">' +
		'<label>MAKE Fred Charlie MOVE Charlie LOCATION door door</label>' +
		'<parameter name="cost" class="numeric">500</parameter>' +
		'<parameter name="likelihood" class="ordinal">L</parameter>' +
		'<parameter name="difficulty" class="ordinal">H</parameter>' +
		'<parameter name="time" class="ordinal">MT</parameter>' +
	'</node>',

	r'( FORCE Fred LOCATION door door)':
	'<node refinement="disjunctive">' +
		'<label> FORCE Fred LOCATION door door</label>' +
		'<parameter name="cost" class="numeric">500</parameter>' +
		'<parameter name="likelihood" class="ordinal">L</parameter>' +
		'<parameter name="difficulty" class="ordinal">H</parameter>' +
		'<parameter name="time" class="ordinal">MT</parameter>' +
	'</node>',

	r'(MAKE Fred Charlie IN Charlie ITEM card x004 ACTOR Margrethe Margrethe)':
	'<node refinement="disjunctive">' +
		'<label>MAKE Fred Charlie IN Charlie ITEM card x004 ACTOR Margrethe Margrethe</label>' +
		'<parameter name="cost" class="numeric">500</parameter>' +
		'<parameter name="likelihood" class="ordinal">L</parameter>' +
		'<parameter name="difficulty" class="ordinal">H</parameter>' +
		'<parameter name="time" class="ordinal">MT</parameter>' +
	'</node>',

	r'(MAKE Fred Margrethe IN Margrethe ITEM card x004 ACTOR Margrethe Margrethe)':
	'<node refinement="disjunctive">' +
		'<label>MAKE Fred Margrethe IN Margrethe ITEM card x004 ACTOR Margrethe Margrethe</label>' +
		'<parameter name="cost" class="numeric">500</parameter>' +
		'<parameter name="likelihood" class="ordinal">L</parameter>' +
		'<parameter name="difficulty" class="ordinal">H</parameter>' +
		'<parameter name="time" class="ordinal">MT</parameter>' +
	'</node>',

	r'( MOVE Fred LOCATION door door)':
	'<node refinement="disjunctive">' +
		'<label> MOVE Fred LOCATION door door</label>' +
		'<parameter name="cost" class="numeric">500</parameter>' +
		'<parameter name="likelihood" class="ordinal">L</parameter>' +
		'<parameter name="difficulty" class="ordinal">H</parameter>' +
		'<parameter name="time" class="ordinal">MT</parameter>' +
	'</node>',

	r'( FULFILL Fred trusts Margrethe )':
	'<node refinement="disjunctive">' +
		'<label> FULFILL Fred trusts Margrethe </label>' +
		'<parameter name="cost" class="numeric">500</parameter>' +
		'<parameter name="likelihood" class="ordinal">L</parameter>' +
		'<parameter name="difficulty" class="ordinal">H</parameter>' +
		'<parameter name="time" class="ordinal">MT</parameter>' +
	'</node>',

	r'(MAKE Fred Charlie FULFILL Charlie trusts Margrethe )':
	'<node refinement="disjunctive">' +
		'<label>MAKE Fred Charlie FULFILL Charlie trusts Margrethe </label>' +
		'<parameter name="cost" class="numeric">500</parameter>' +
		'<parameter name="likelihood" class="ordinal">L</parameter>' +
		'<parameter name="difficulty" class="ordinal">H</parameter>' +
		'<parameter name="time" class="ordinal">MT</parameter>' +
	'</node>',

	r'(\s*IN Fred ITEM card x004 ACTOR Margrethe Margrethe)':
	'<node refinement="disjunctive">' +
		'<label>IN Fred ITEM card x004 ACTOR Margrethe Margrethe</label>' +
		'<parameter name="cost" class="numeric">500</parameter>' +
		'<parameter name="likelihood" class="ordinal">L</parameter>' +
		'<parameter name="difficulty" class="ordinal">H</parameter>' +
		'<parameter name="time" class="ordinal">MT</parameter>' +
	'</node>',

	r'(MAKE Fred Charlie FORCE Charlie LOCATION door door)':
	'<node refinement="disjunctive">' +
		'<label>MAKE Fred Charlie FORCE Charlie LOCATION door door</label>' +
		'<parameter name="cost" class="numeric">500</parameter>' +
		'<parameter name="likelihood" class="ordinal">L</parameter>' +
		'<parameter name="difficulty" class="ordinal">H</parameter>' +
		'<parameter name="time" class="ordinal">MT</parameter>' +
	'</node>',

}