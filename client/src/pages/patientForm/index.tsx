import React, { useEffect, useState } from 'react';
import { makeStyles } from '@material-ui/core/styles';
import { PatientForm } from './PatientForm';
import { useRouteMatch } from 'react-router-dom';
import { getPatientState, PatientState } from './state';
import LinearProgress from '@material-ui/core/LinearProgress';

type RouteParams = {
  patientId: string | undefined;
  editId: string;
  universalRecordId: string | undefined;
};

export const PatientFormPage = () => {
  const classes = useStyles();
  //universalRecordId stands for pregnancyId and medicalRecordId because they share the same route matching
  const { patientId, editId, universalRecordId } =
    useRouteMatch<RouteParams>().params;

  const [formInitialState, setFormInitialState] = useState<PatientState>();

  useEffect(() => {
    getPatientState(patientId, universalRecordId, editId).then((state) =>
      setFormInitialState(state)
    );
  }, [patientId, editId, universalRecordId]);

  return (
    <div className={classes.container}>
      {formInitialState === undefined ? (
        <LinearProgress />
      ) : (
        <PatientForm
          initialState={formInitialState}
          patientId={patientId}
          pregnancyId={universalRecordId}
          creatingNew={patientId === undefined}
          creatingNewPregnancy={
            patientId !== undefined && universalRecordId === undefined
          }
          editId={editId}
          universalRecordId={universalRecordId}
        />
      )}
    </div>
  );
};

const useStyles = makeStyles({
  container: {
    maxWidth: 1250,
    margin: '0 auto',
  },
});