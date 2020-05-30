/*
A KBase module: jsf_action_test
This sample module contains one small method that filters contigs.
*/

module jsf_action_test {
    typedef structure {
        string report_name;
        string report_ref;
    } ReportResults;

    /*
        This example function accepts any number of parameters and returns results in a KBaseReport
    */
    funcdef run_jsf_action_test(mapping<string,UnspecifiedObject> params) returns (ReportResults output) authentication required;

};
