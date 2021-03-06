# -*- coding: utf-8 -*-
#
# This file is part of INSPIRE.
# Copyright (C) 2016 CERN.
#
# INSPIRE is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# INSPIRE is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with INSPIRE. If not, see <http://www.gnu.org/licenses/>.
#
# In applying this licence, CERN does not waive the privileges and immunities
# granted to it by virtue of its status as an Intergovernmental Organization
# or submit itself to any jurisdiction.

from __future__ import absolute_import, division, print_function

from dojson.utils import GroupableOrderedDict

from inspirehep.modules.authors.dojson.model import updateform


def test_name_status_from_status():
    form = GroupableOrderedDict([
        ('status', 'foo'),
    ])

    expected = {
        'status': 'foo',
    }
    result = updateform.do(form)

    assert expected == result['name']


def test_name_status_from_status_updates():
    form = GroupableOrderedDict([
        ('status', 'foo'),
        ('status', 'bar'),
    ])

    expected = {
        'status': 'bar',
    }
    result = updateform.do(form)

    assert expected == result['name']


def test_name_preferred_name_from_display_name():
    form = GroupableOrderedDict([
        ('display_name', 'foo'),
    ])

    expected = {
        'preferred_name': 'foo',
    }
    result = updateform.do(form)

    assert expected == result['name']


def test_name_preferred_name_from_display_name_updates():
    form = GroupableOrderedDict([
        ('display_name', 'foo'),
        ('display_name', 'bar'),
    ])

    expected = {
        'preferred_name': 'bar',
    }
    result = updateform.do(form)

    assert expected == result['name']


def test_urls_from_websites_webpage():
    form = {
        'websites': [
            {
                'webpage': 'foo',
            },
        ],
    }

    expected = [
        {
            'description': '',
            'value': 'foo',
        },
    ]
    result = updateform.do(form)

    assert expected == result['urls']


def test_urls_from_twitter_url():
    form = GroupableOrderedDict([
        ('twitter_url', 'foo'),
    ])

    expected = [
        {
            'description': 'TWITTER',
            'value': 'foo',
        },
    ]
    result = updateform.do(form)

    assert expected == result['urls']


def test_urls_from_twitter_url_appends():
    form = GroupableOrderedDict([
        ('twitter_url', 'foo'),
        ('twitter_url', 'bar'),
    ])

    expected = [
        {
            'description': 'TWITTER',
            'value': 'foo',
        },
        {
            'description': 'TWITTER',
            'value': 'bar',
        },
    ]
    result = updateform.do(form)

    assert expected == result['urls']


def test_urls_from_blog_url():
    form = GroupableOrderedDict([
        ('blog_url', 'foo'),
    ])

    expected = [
        {
            'description': 'BLOG',
            'value': 'foo',
        },
    ]
    result = updateform.do(form)

    assert expected == result['urls']


def test_urls_from_blog_url_appends():
    form = GroupableOrderedDict([
        ('blog_url', 'foo'),
        ('blog_url', 'bar'),
    ])

    expected = [
        {
            'description': 'BLOG',
            'value': 'foo',
        },
        {
            'description': 'BLOG',
            'value': 'bar',
        },
    ]
    result = updateform.do(form)

    assert expected == result['urls']


def test_urls_from_linkedin_url():
    form = GroupableOrderedDict([
        ('linkedin_url', 'foo'),
    ])

    expected = [
        {
            'description': 'LINKEDIN',
            'value': 'foo',
        },
    ]
    result = updateform.do(form)

    assert expected == result['urls']


def test_urls_from_linkedin_url_appends():
    form = GroupableOrderedDict([
        ('linkedin_url', 'foo'),
        ('linkedin_url', 'bar'),
    ])

    expected = [
        {
            'description': 'LINKEDIN',
            'value': 'foo',
        },
        {
            'description': 'LINKEDIN',
            'value': 'bar',
        },
    ]
    result = updateform.do(form)

    assert expected == result['urls']


def test_ids_from_orcid():
    form = GroupableOrderedDict([
        ('orcid', 'foo'),
    ])

    expected = [
        {
            'type': 'ORCID',
            'value': 'foo',
        },
    ]
    result = updateform.do(form)

    assert expected == result['ids']


def test_ids_from_orcid_appends():
    form = GroupableOrderedDict([
        ('orcid', 'foo'),
        ('orcid', 'bar'),
    ])

    expected = [
        {
            'type': 'ORCID',
            'value': 'foo',
        },
        {
            'type': 'ORCID',
            'value': 'bar',
        },
    ]
    result = updateform.do(form)

    assert expected == result['ids']


def test_ids_from_bai():
    form = GroupableOrderedDict([
        ('bai', 'foo'),
    ])

    expected = [
        {
            'type': 'BAI',
            'value': 'foo',
        },
    ]
    result = updateform.do(form)

    assert expected == result['ids']


def test_ids_from_bai_appends():
    form = GroupableOrderedDict([
        ('bai', 'foo'),
        ('bai', 'bar'),
    ])

    expected = [
        {
            'type': 'BAI',
            'value': 'foo',
        },
        {
            'type': 'BAI',
            'value': 'bar',
        },
    ]
    result = updateform.do(form)

    assert expected == result['ids']


def test_ids_from_inspireid():
    form = GroupableOrderedDict([
        ('inspireid', 'foo'),
    ])

    expected = [
        {
            'type': 'INSPIRE',
            'value': 'foo',
        },
    ]
    result = updateform.do(form)

    assert expected == result['ids']


def test_ids_from_inspireid_appends():
    form = GroupableOrderedDict([
        ('inspireid', 'foo'),
        ('inspireid', 'bar'),
    ])

    expected = [
        {
            'type': 'INSPIRE',
            'value': 'foo',
        },
        {
            'type': 'INSPIRE',
            'value': 'bar',
        },
    ]
    result = updateform.do(form)

    assert expected == result['ids']


def test_positions_from_public_email():
    form = GroupableOrderedDict([
        ('public_email', 'foo'),
    ])

    expected = [
        {
            'current': 'Current',
            'email': 'foo',
        },
    ]
    result = updateform.do(form)

    assert expected == result['positions']


def test_positions_from_public_email_appends():
    form = GroupableOrderedDict([
        ('public_email', 'foo'),
        ('public_email', 'bar'),
    ])

    expected = [
        {
            'current': 'Current',
            'email': 'foo',
        },
        {
            'current': 'Current',
            'email': 'bar',
        },
    ]
    result = updateform.do(form)

    assert expected == result['positions']


def test_field_categories_from_research_field():
    form = GroupableOrderedDict([
        ('research_field', 'foo'),
    ])

    expected = [
        {
            'source': 'submitter',
            'term': 'foo',
        },
    ]
    result = updateform.do(form)

    assert expected == result['field_categories']


def test_positions_from_institutions_history():
    form = {
        'institution_history': [
            {
                'start_year': 2009,
                'end_year': 2010,
                'name': 'foo',
                'email': 'bar',
                'old_email': 'baz',
                'current': 'qux',
                'rank': 'quux',
            },
            {
                'start_year': 2010,
                'end_year': 2012,
                'name': 'oof',
                'email': 'rab',
                'old_email': 'zab',
                'current': '',
                'rank': 'rank',
            },
        ],
    }

    expected = [
        {
            'institution': {'name': 'oof'},
            'status': '',
            'start_date': 2010,
            'end_date': 2012,
            'email': 'rab',
            'old_email': 'zab',
            'rank': '',
        },
        {
            'institution': {'name': 'foo'},
            'status': 'current',
            'start_date': 2009,
            'end_date': 2010,
            'email': 'bar',
            'old_email': 'baz',
            'rank': 'quux',
        },
    ]
    result = updateform.do(form)

    assert expected == result['positions']


def test_phd_advisors_from_advisors():
    form = {
        'advisors': [
            {
                'degree_type': 'PhD',
                'full_name': '',
            },
            {
                'degree_type': 'PhD',
                'full_name': 'foo',
            },
        ],
    }

    expected = [
        {
            'degree_type': 'PhD',
            'name': 'foo',
        },
    ]
    result = updateform.do(form)

    assert expected == result['phd_advisors']


def test_experiments_from_experiments():
    form = {
        'experiments': [
            {
                'start_year': 2009,
                'status': 'foo',
            },
            {
                'start_year': 2010,
                'status': '',
            },
        ],
    }

    expected = [
        {
            'start_year': 2010,
            'status': ''
        },
        {
            'start_year': 2009,
            'status': 'current',
        },
    ]
    result = updateform.do(form)

    assert expected == result['experiments']
